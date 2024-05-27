# data_fetching/Dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY fetch_weather_data.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "fetch_weather_data.py"]
