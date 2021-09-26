# How to
The project does not use any other dependencies. You just need to install pytest and run the command `pytest`
in order to launch the integration tests

# Design
The design can be seen in the integration test file

* The first component is `pubmed_format`. It takes a folder that can have csv or json file, and merge into
one file in `pubmed_clean` folder. The goal is to have an unified data format
* The second component is `pubmed_drug` which aggregate data between pubmed and drug.
* The third component is `clinical_trials_drug` which find the relationship between clinical trials and drug.
* The forth component is `journal_drug` which uses the output from the second and third component, merge the result
into a file

The second and third component can be run in parallel

In real world, each component can be implemented by Azure Durable Function, Kubernetes Argo workflow.
The thing to do is to package these files in appropriated format (Azure function files or docker image)
And the API can be implemented with fast-api
I don't have time to implement the diff algorithm. If the data is not important and/or the frequency of refresh
is not high, we can accept to run a full ingestion without any problem. To implement the diff feature, we need to detect
if the file is never ingested into the pipeline, and then send these files as input of the data pipeline
