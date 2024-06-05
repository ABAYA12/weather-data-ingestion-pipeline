# airflow/Dockerfile
FROM apache/airflow:2.1.2

# Copy DAGs
COPY airflow/dags /opt/airflow/dags

# Copy data fetching scripts
COPY data_fetching/fetch_weather_data.py /app/fetch_weather_data.py
COPY data_fetching/requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r /app/requirements.txt
