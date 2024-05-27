# airflow/Dockerfile
FROM apache/airflow:2.1.2
COPY dags /opt/airflow/dags
COPY data_fetching/fetch_weather_data.py /app/fetch_weather_data.py
COPY data_fetching/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
