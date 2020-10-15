# airflow-tutorial
In this tutorial you will learn what Airflow is, why you should use it and how to set it up.

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

