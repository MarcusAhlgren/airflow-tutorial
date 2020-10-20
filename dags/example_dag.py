import datetime as dt

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from src.process_raw_data import preprocess
from src.make_predictions import predict


default_args = {
    'owner': 'Marcus',
    'start_date': dt.datetime(2020, 1, 1),
    'depends_on_past': False,
    'email': ['marcus.ahlgren@combient.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': dt.timedelta(minutes = 5)
}

dag = DAG('example_dag',
         default_args=default_args,
         schedule_interval='*/5 * * * *',
         catchup = False
         )

task1 = PythonOperator(task_id = 'process_raw_data',
                       python_callable = preprocess,
                       dag = dag)

task2 = PythonOperator(task_id = 'make_predictions',
                       python_callable = predict,
                       dag = dag)

task1 >> task2