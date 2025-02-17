# Ploomber sample projects

![CI](https://github.com/ploomber/projects/workflows/ci/badge.svg)

<p align="center">
  <a href="https://ploomber.io/community">Join our community</a>
  |
  <a href="https://share.hsforms.com/1E7Qa_OpcRPi_MV-segFsaAe6c2g">Newsletter</a>
  |
  <a href="https://docs.ploomber.io/">Docs</a>
  |
  <a href="https://twitter.com/intent/user?screen_name=ploomber">Twitter</a>
  |
  <a href="https://ploomber.io/">Blog</a>
  |
  <a href="https://www.youtube.com/channel/UCaIS5BMlmeNQE4-Gn0xTDXQ">YouTube</a>
  |
  <a href="mailto:contact@ploomber.io">Contact us</a>
</p>

This repository contains sample pipelines developed using [Ploomber](https://github.com/ploomber/ploomber).

**Note:** We recommend you to go through the [first tutorial](https://docs.ploomber.io/en/latest/get-started/first-pipeline.html) to learn the basics of Ploomber.

## Running examples


Use Colab:

<p align="center">
    <a href="https://colab.research.google.com/github/ploomber/projects/blob/master/guides/first-pipeline/colab.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
</p>

Use Binder (free, hosted JupyterLab):

[![Binder](https://raw.githubusercontent.com/ploomber/projects/master/_static/open-in-jupyterlab.svg)](https://binder.ploomber.io/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252FREADME.ipynb%26branch%3Dmaster)

Or run locally:

~~~sh
pip install ploomber

# list examples
ploomber examples

# download example with name
ploomber examples --name {name}

# example
ploomber examples --name templates/mlflow
~~~

## How to read the examples

Each example contains a `README.md` file that describes it; a `README.ipynb` is also available with the same contents but in Jupyter notebook format and with command outputs. In addition, files for `pip` (`requirements.txt`) and  `conda` (`environment.yml`) are provided for local execution.

## Index

### Templates

Starting points for common use cases. Use them to ramp up a project quickly.


1. [`templates/etl`](templates/etl/README.ipynb) Download a data file, upload it to a database, process it, and plot with Python and R.

2. [`templates/exploratory-analysis`](templates/exploratory-analysis/README.ipynb) Sample pipeline that explores penguins data.

3. [`templates/google-cloud`](templates/google-cloud/README.ipynb) Use Google Cloud and Ploomber to develop a scalable and production-ready pipeline.

4. [`templates/ml-advanced`](templates/ml-advanced/README.ipynb) ML pipeline using the Python API. Shows how to create a Python package, test it with pytest, and train models in parallel.

5. [`templates/ml-basic`](templates/ml-basic/README.ipynb) Download data, clean it, generate features and train a model.

6. [`templates/ml-intermediate`](templates/ml-intermediate/README.ipynb) Training and serving ML pipelines with integration testing to evaluate training data quality.

7. [`templates/ml-online`](templates/ml-online/README.ipynb) Load data, generate features, train a model, and deploy model with flask.

8. [`templates/mlflow`](templates/mlflow/README.ipynb) Train a grid of models and log them to MLflow.

9. [`templates/python-api`](templates/python-api/README.ipynb) Loads, clean, and plot data using the Python API.

10. [`templates/pytorch`](templates/pytorch/README.ipynb) Using GPUs to train models in Ploomber Cloud.

11. [`templates/shell`](templates/shell/README.ipynb) Create a pipeline with shell scripts as tasks.

12. [`templates/spec-api-directory`](templates/spec-api-directory/README.ipynb) Create a pipeline from a directory with scripts (without a pipeline.yaml file).

13. [`templates/spec-api-r`](templates/spec-api-r/README.ipynb) Load, clean and plot data with R.

14. [`templates/spec-api-sql`](templates/spec-api-sql/README.ipynb) Use SQL scripts to manipulate data in a database, dump a table, and plot it with Python.


### Cookbook

Short and to-the-point examples showing how to use a specific feature.


2. [`cookbook/dynamic-params`](cookbook/dynamic-params/README.ipynb) Pipeline parameters whose values are computed at runtime.

3. [`cookbook/file-client`](cookbook/file-client/README.ipynb) Upload task's products upon execution (local, S3, GCloud storage)

4. [`cookbook/grid`](cookbook/grid/README.ipynb) An example showing how to create a grid of tasks to train models with different parameters.

5. [`cookbook/hooks`](cookbook/hooks/README.ipynb) Task hooks

6. [`cookbook/incremental`](cookbook/incremental/README.ipynb) A pipeline that processes new records from a database and uploads them.

7. [`cookbook/nested-cv`](cookbook/nested-cv/README.ipynb) Nested cross-validation for model selection and hyperparameter tuning.

8. [`cookbook/python-load`](cookbook/python-load/README.ipynb) Load pipeline.yaml file in a Python session to customize initialization.

9. [`cookbook/report-generation`](cookbook/report-generation/README.ipynb) Generating HTML/PDF reports.

10. [`cookbook/serialization`](cookbook/serialization/README.ipynb) Shows how to use the serializer and unserializer decorators.

11. [`cookbook/sql-dump`](cookbook/sql-dump/README.ipynb) A minimal example showing how to dump a table from a SQL database.

13. [`cookbook/variable-number-of-products`](cookbook/variable-number-of-products/README.ipynb) Shows how to create tasks whose number of products depends on runtime conditions.


### Guides

In-depth tutorials for learning.  These are part of the [documentation](https://docs.ploomber.io/en/latest/user-guide/index.html).


5. [`guides/cron`](guides/cron/README.ipynb) This guide shows how to schedule Ploomber pipelines using cron.

6. [`guides/debugging`](guides/debugging/README.ipynb) Tutorial showing techniques for debugging pipelines.

7. [`guides/first-pipeline`](guides/first-pipeline/README.ipynb) Introductory tutorial to learn the basics of Ploomber.

8. [`guides/intro-to-ploomber`](guides/intro-to-ploomber/README.ipynb) Introductory tutorial to learn the basics of Ploomber.

9. [`guides/logging`](guides/logging/README.ipynb) Tutorial showing how to add logging to a pipeline.

10. [`guides/parametrized`](guides/parametrized/README.ipynb) Tutorial showing how to parametrize pipelines and change parameters from the command-line.

11. [`guides/refactor`](guides/refactor/README.ipynb) Using Soorgeon to convert a notebook into a Ploomber pipeline.

12. [`guides/serialization`](guides/serialization/README.ipynb) Tutorial explaining how the serializer and unserializer fields in a pipeline.yaml file work.

13. [`guides/sql-templating`](guides/sql-templating/README.ipynb) Introductory tutorial teaching how to develop modular SQL pipelines.

14. [`guides/testing`](guides/testing/README.ipynb) Tutorial showing how to use a task's on_finish hook to test data quality.

15. [`guides/versioning`](guides/versioning/README.ipynb) A tutorial showing how to version pipeline products.



## Python API

The simplest way to get started with Ploomber is via the Spec API, which allows you to describe pipelines using a `pipeline.yaml` file, most examples on this repository use the Spec API. However, if you want more flexibility, you may write pipelines with Python.

The [`templates/python-api/`](templates/python-api) directory contains a project written using the Python API. And the [`python-api-examples/`](python-api-examples) includes some tutorials and more examples.


## Micro-pipelines

In Ploomber `0.21`, we introduced a simplified API to write pipelines in a single Jupyter notebook (or `.py`) file. This is a great option for small projects.

You can find the examples in the [`micro-pipelines/`](micro-pipelines) directory.