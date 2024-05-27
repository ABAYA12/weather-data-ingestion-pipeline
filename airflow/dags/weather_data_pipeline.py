# airflow/dags/weather_data_pipeline.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
}

with DAG(
    'weather_data_pipeline',
    default_args=default_args,
    description='A simple weather data ingestion pipeline',
    schedule_interval='@hourly',
    start_date=days_ago(1),
    catchup=False,
) as dag:

    fetch_weather_data = BashOperator(
        task_id='fetch_weather_data',
        bash_command='python /app/fetch_weather_data.py',
    )
