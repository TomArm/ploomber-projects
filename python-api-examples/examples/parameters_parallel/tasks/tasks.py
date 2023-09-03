"""This file contains tasks to be used to demonstrate paralelising a DAG.
The tasks's themselves are not intended to be representative of useful workloads,
instead, they are intended to demonstrate how a parallelised DAG can be created 
using the Python API
"""

import os
import numpy as np
import pandas as pd
from ploomber.products import File


def _make_data_stream(n_entries=100):
    """Make the data for a stream. 
    This function is intended for calling by other functions whihc are ploomber tasks 

    Args:
        n_entries (int, optional): The number of values to return for the data. Defaults to 100.

    Returns:
        _type_: returns a tuple of t and f values for the data stream
    """
    stream_t = np.linspace(0, 100, n_entries)

    slope = np.random.uniform(0, 0.1)

    periodic_freq = np.random.uniform(1, n_entries / 2)
    periodic_scale = np.random.uniform(0, 1)

    stream_f = (
        slope * stream_t
        + periodic_scale * np.sin(stream_t / periodic_freq)
        + np.random.exponential(scale=0.5, size=n_entries)
    )

    return stream_t, stream_f


def make_multi_data(
    product: File,
    n_streams: int = 2,
    n_entries: int = 100,
) -> None:
    """Makes a datafile containing multiple series
    For use when running the parallelised DAG (using the python API)

    Args:
        product (File): Location of the csv output file
        n_streams (int, optional): _description_. Defaults to 2.
        n_entries (int, optional): The number of values to return for the data. Defaults to 100.

    """
    df = pd.DataFrame()

    for i in range(n_streams):
        stream_name = f"stream-{i:03d}"
        stream_t, stream_f = _make_data_stream(n_entries)
        if not "t" in df.columns:
            df["t"] = stream_t
        df[stream_name] = stream_f
        file_name = f"{stream_name}.csv"

    file_name = product
    df.to_csv(file_name, index=False)


def make_single_data(product: File, n_entries=100) -> None:
    """Makes a data file with a single data series.
    For use when running a single branch (e.g. with `ploomber build` and the `pipeline.yaml`)

    Args:
        product (File): Location of the csv output file
        n_entries (int, optional): The number of values to return for the data. Defaults to 100.
    """
    stream_t, stream_f = _make_data_stream(n_entries)
    df = pd.DataFrame(data={"t": stream_t, "f": stream_f})

    df.to_csv(os.path.join(product), index=False)


def extract_data_subset(upstream: dict, product: dict, name: str) -> None:
    """Extracts a single result from the cominbed data stream

    Args:
        upstream (dict): Upstream tasks (provided by Ploomber)
        product (dict): Products (provided by Ploomber)
        name (str): Name of the data stream (csv column) to extract
    """
    data_file = upstream["make-data"]
    df = pd.read_csv(data_file)

    df_subset = df[["t", name]].rename({name: "f"}, axis="columns")
    df_subset.to_csv(product, index=False)


def integration(upstream: dict, product) -> None:
    """Integrates the data to determine the area under the curve

    Args:
        upstream (dict): Upstream tasks (provided by Ploomber)
        product (dict): Products (provided by Ploomber)
    """


    # The code below handles the case where the task is called either as a stand alone task in a serial DAG, or as part of a parallel DAG.
    # When called in parallel, the upstream variable is overwritten and is replaced by a nested dictionary 
    # with keys corresponding to the name of the upstream task.
    upstream_file = upstream["filter-data"]

    if "file" in upstream_file:
        input_file = str(upstream_file["file"])
    else:
        input_file = list(upstream_file.values())[0]["file"]



    # Read the data from csv and use numpy to integrate it with the trapezium rule.
    df = pd.read_csv(input_file)
    area = np.trapz(df["f"], df["t"])

    # Output the data to a file
    output_file = product["file"]
    df_area = pd.DataFrame(data={"area": [area]})
    df_area.to_csv(output_file, index=False)


def totaliser(upstream: dict, product: dict) -> None:
    """A task to sum the results of each parallel branch of the DAG and create a file with the total

    Args:
        upstream (dict): Upstream tasks (provided by Ploomber)
        product (dict): Products (provided by Ploomber)
    """

    total = 0

    for key, item in upstream.items():
        df = pd.read_csv(item["file"])
        total = total + df["area"][0]

    with open(product["file"], "w") as f:
        f.write(f"{total:.3f}")
