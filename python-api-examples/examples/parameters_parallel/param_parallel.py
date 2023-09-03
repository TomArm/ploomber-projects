"""
Parametrized DAGs
=================

This example shows how to take parameterise a series of tasks.
The individual tasks are not intended to be representative of actual workloads, instead, 
this example focuses on a process for creating a parallel DAG

e.g 


    |--> B1 --> C1 --> D1 -->|
    |--> B2 --> C2 --> D2 -->|
A --|     ....               |--> E
    |--> Bn --> Cn --> Dn -->|

"""


import numpy as np


import pandas as pd

from pathlib import Path
import os
import glob
import tempfile

from ploomber import DAG
from ploomber.tasks import PythonCallable, NotebookRunner, Task
from ploomber.executors import Parallel
from ploomber.products import File


import matplotlib.pyplot as plt

from tasks.tasks import make_multi_data, integration, totaliser, extract_data_subset


def make_processor_pipeline(stream_name: str, make_data_task: Task, dag: DAG) -> Task:
    """Function to generate a pipeline of tasks to be run for a single stream of the data.
        This will be called multiple times to generate parallel sections of the DAG.

    Args:
        stream_name (str): An ID used to name this stream of the parallel DAG. The name needs to correspond to a column in the combined data file
        make_data_task (Task): The upstream task that generates the data to be processed by the parallel section of the pipeline
        dag (DAG): Ploomber DAG to add the tasks to

    Returns:
        Task: Returns the final taks. This enables it to be passed into the input of subsequent tasks after the parallel section of the DAG
    """


    # Generate a task to extract the data for this parallel stream from the main data file
    extract_data_subset_task = PythonCallable(
        extract_data_subset,
        dag=dag,
        name=f"{stream_name}_extract_data",
        params={"name": stream_name},
        product=File(os.path.join(products_dir, f"{stream_name}.csv")),
    )

    # Process the data using a notebook to remove outliers
    filter_data_task = NotebookRunner(
        source=Path(os.path.join("tasks", "filter_data.py")),
        dag=dag,
        name=f"{stream_name}_filter-data",
        product={
            "nb": File(os.path.join(products_dir, f"{stream_name}_filter_data.ipynb")),
            "file": File(os.path.join(products_dir, f"{stream_name}_cleaned.csv")),
        },
    )

    # Integrate the data to find the area under the curve
    integrate_data_task = PythonCallable(
        integration,
        dag=dag,
        name=f"{stream_name}_area",
        product={"file": File(os.path.join(products_dir, f"{stream_name}_area.csv"))},
    )

    # Override the `upstream` variables for the tasks we've created to make them specific to this branch 
    filter_data_task.set_upstream(extract_data_subset_task, "make-data")
    integrate_data_task.set_upstream(filter_data_task, "filter-data")

    # Make the sub section of the DAG by linking the tasks together
    (
        make_data_task
        >> extract_data_subset_task
        >> filter_data_task
        >> integrate_data_task
    )

    # Return the last task so it can be added to the inputs of the summarisation task
    return integrate_data_task


if __name__ == "__main__":

    # Number of parallel streams to create
    n_streams = 3

    # Set up the directory to hold products from the pipeline
    products_dir = os.path.join(os.path.curdir, "products", "multi")
    if not os.path.exists(products_dir):
        os.mkdir(products_dir)


    # Create the DAG and set options
    dag = DAG()
    dag.executor = Parallel()


    # Create the upstream task to generate the combined data file
    make_data_task = PythonCallable(
        make_multi_data,
        name="make-data",
        product=File(os.path.join(products_dir, "input_data.csv")),
        dag=dag,
        params={"n_streams": n_streams},
    )

    
    # Loop through each stream and make the parallel section of the DAG.
    # Add the integration task to the array so we can use it later when summing up all the results
    stream_integration_tasks = []
    for i in range(n_streams):
        stream_integration_task = make_processor_pipeline(
            f"stream-{i:03d}", make_data_task, dag
        )
        stream_integration_tasks.append(stream_integration_task)
    

    # Create the final task to sum the values created in each of the parallel sections of the DAG
    totaliser_task = PythonCallable(
        totaliser,
        dag=dag,
        name="totaliser",
        product={"file": File(os.path.join(products_dir, "total.txt"))},
    )

    # Add each of the individual stream's outputs as an input to the totaliser
    for t in stream_integration_tasks:
        t >> totaliser_task
        totaliser_task.set_upstream(t)

    # Make a plot of the DAG
    dag.plot("param_parallel.html", backend="mermaid")

    # Run the DAG and generate results
    dag.build()
