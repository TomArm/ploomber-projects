# Parallel Parameterised Pipelines

This example shows how to run a pipeline in parallel for multiple parameters.

E.g


```mermaid
graph LR
    A --> B1 --> C1 --> D1 --> E 
    A --> B2 --> C2 --> D2 --> E 
    A --> B3 --> C3 --> D3 --> E 
    A --> B... --> C... --> D... --> E 
    A --> Bn --> Cn --> Dn --> E 
```

A `pipeline.yaml` file is included to allow a single branch to be run.
The demonstration pipeline includes both Notebook and python callable tasks.


## Running 


The example can be run either for a single branch using `ploomber build`, or for the full parallel DAG with `python param_parallel.py` 

