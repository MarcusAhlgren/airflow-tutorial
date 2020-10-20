FROM puckel/docker-airflow:1.10.9
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt