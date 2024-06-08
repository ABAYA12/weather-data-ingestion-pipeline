import requests  # Library for making HTTP requests
import pandas as pd  # Library for data manipulation and analysis
from sqlalchemy import create_engine  # Library for database interaction
from datetime import datetime  # Module for working with dates and times
import os  # Module for accessing environment variables

# Getting the OpenWeatherMap API key from environment variables
API_KEY = os.getenv('OPENWEATHER_API_KEY')

# List of cities for which weather data will be fetched
CITIES = ["London", "New York", "Tokyo", "Sydney", "Mumbai", "Accra"]

def fetch_weather_data(city):
    """
    Fetches weather data for a given city from the OpenWeatherMap API.

    Args:
        city (str): The name of the city for which weather data is to be fetched.

    Returns:
        dict: A dictionary containing relevant weather data for the city.
    """
    # Constructing the URL for OpenWeatherMap API call
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    # Sending HTTP GET request to the API
    response = requests.get(url)
    # Parsing JSON response
    data = response.json()
# Returning a dictionary containing relevant weather data for the city
    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "date": datetime.now().strftime('%Y-%m-%d'),  # Current date
        "time": datetime.now().strftime('%H:%M:%S')   # Current time
    }

def main():
    """
    Main function to fetch weather data for multiple cities and store it in a PostgreSQL database.
    """
    # Fetching weather data for all cities in the list
    weather_data = [fetch_weather_data(city) for city in CITIES]
    # Creating a DataFrame from the fetched data
    df = pd.DataFrame(weather_data)
    # Creating a SQLAlchemy engine to connect to the PostgreSQL database
    engine = create_engine('postgresql://postgres:password@database:5432/weather')
    # Writing the DataFrame to the database table 'weather_data'
    # if_exists='append' specifies that if the table exists, data will be appended to it
    df.to_sql('weather_data', engine, if_exists='append', index=False)

# Entry point of the script
if __name__ == "__main__":
    main()  # Calling the main function when the script is executed directly
