# airflow-tutorial
In this tutorial you will learn what Airflow is, why you should use it and how to set it up. The repo also a an example machine learning pipeline built with Airflow in a dockerized format. See section **Example Pipeline**.

## Introduction

Airflow is a a platform for creating, scheduling and monitoring workflows. The development of the platform started in 2014 in Airbnb as an open source project. The platform was further developed as an Apache Incubator project and as of 2019 it is an Apache Software Foundation project. The workflows can be thought of as a sequence of tasks and are defined in Python scripts. The workflows can be run on schedule or triggered by events e.g. new files ingested in database. Airflow also provides a UI which allows users to easily get an overview of the workflows and their status.

## Terminology

### DAG

DAG is an acronym for directed acyclic graph. The nodes in the graph are your tasks(scripts) and the direction between them indicate in which order they should be run. 
DAGs are the objects defining workflows in Airflow and they are written in Python scripts.

### Operators

The tasks in a DAG are defined with objects called operators. There many predefined operators in Airflow such as:

* BashOperator - Executes a bash command.
* PythonOperator - Executes a Python function.
* MySqlOperator - Executes SQL query.

There is also the possibility to create customized operators tailored for your needs.

### Sensors

Sensors are similar to Operators but they only run if certain conditions are fulfilled. An example sensor is the S3KeySensor which looks for a given file in an S3 bucket and is triggered if the file is found.

## Setup

Now that we have knowledge about the core concepts of Airflow it's time to set it up. Airflow is installed with `pip` using the command 
    pip install apache-airflow
Before we can use Airflow we need to initiate its database which will hold all the information about the workflows. The location where Airflow will setup this database is stored in the environment variable `AIRFLOW_HOME`. To create a folder `airflow` in your current directory to hold the Airflow database run the command

    export AIRFLOW_HOME="$(pwd)/airflow"

Now to initiate the database in the set location we simply run

    airflow initdb
and 

    airflow webserver -p 8080
to start the web server for the UI. The UI is now accessible at `localhost:8080` in your browser.

## Example Pipeline

To run the example pipeline perform the following steps.

1. Clone this repo.

2. Build and run the docker image.

        docker-compose up
    
3. Go to the webserver at `localhost:8080` in your browser to access the Airflow UI.

    


    

