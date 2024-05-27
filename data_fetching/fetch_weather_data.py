import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import os

API_KEY = os.getenv('OPENWEATHER_API_KEY')
CITIES = ["London", "New York", "Tokyo", "Sydney", "Mumbai"]


def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={
        city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "datetime": datetime.now()
    }


def main():
    weather_data = [fetch_weather_data(city) for city in CITIES]
    df = pd.DataFrame(weather_data)
    engine = create_engine(
        'postgresql://postgres:password@database:5432/weather')
    df.to_sql('weather_data', engine, if_exists='append', index=False)


if __name__ == "__main__":
    main()
