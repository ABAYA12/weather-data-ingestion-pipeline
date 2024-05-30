import requests
from datetime import datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

def get_weather(api_key, city):
    # Base URL for OpenWeather API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API call
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    # Make a GET request to the API
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        
        # Extract relevant information
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M:%S')
        }
        
        return weather
    else:
        # Handle errors
        return {'error': f"Failed to get weather data for {city}"}

# Replace 'your_api_key' with your actual OpenWeather API key
api_key = 'your_api_key'  # Replace with your actual API key
cities = ["London", "New York", "Tokyo", "Sydney", "Mumbai"]

# Get weather data for all cities
weather_data_list = []
for city in cities:
    weather_data = get_weather(api_key, city)
    weather_data_list.append(weather_data)

# Convert the list of dictionaries to a DataFrame
weather_df = pd.DataFrame(weather_data_list)

# Save the DataFrame to a CSV file
weather_df.to_csv('weather_data.csv', index=False)

# Plotly Interactive Visualizations

# Temperature by City
fig_temp = px.bar(weather_df, x='city', y='temperature', title='Temperature by City',
                  labels={'temperature': 'Temperature (°C)'}, 
                  hover_data={'temperature': ':.2f°C'})
fig_temp.update_traces(marker_color='skyblue')
fig_temp.update_layout(xaxis_title='City', yaxis_title='Temperature (°C)')

# Humidity by City
fig_humidity = px.bar(weather_df, x='city', y='humidity', title='Humidity by City',
                      labels={'humidity': 'Humidity (%)'}, 
                      hover_data={'humidity': ':.2f%'})
fig_humidity.update_traces(marker_color='lightgreen')
fig_humidity.update_layout(xaxis_title='City', yaxis_title='Humidity (%)')

# Wind Speed by City
fig_wind = px.bar(weather_df, x='city', y='wind_speed', title='Wind Speed by City',
                  labels={'wind_speed': 'Wind Speed (m/s)'}, 
                  hover_data={'wind_speed': ':.2f m/s'})
fig_wind.update_traces(marker_color='lightcoral')
fig_wind.update_layout(xaxis_title='City', yaxis_title='Wind Speed (m/s)')

# Weather Description plot
fig_description = px.histogram(weather_df, x='description', title='Weather Description Count',
                               labels={'description': 'Description', 'count': 'Count'},
                               category_orders={"description": weather_df['description'].value_counts().index})
fig_description.update_traces(marker_color='orange')
fig_description.update_layout(xaxis_title='Description', yaxis_title='Count')

# Display the visualizations
fig_temp.show()
fig_humidity.show()
fig_wind.show()
fig_description.show()

# Enhanced Visualization using Seaborn and Matplotlib
def seaborn_visualizations(weather_df):
    plt.figure(figsize=(14, 8))

    # Temperature plot
    plt.subplot(2, 2, 1)
    sns.barplot(x='city', y='temperature', data=weather_df, palette='coolwarm')
    plt.title('Temperature by City')
    plt.xlabel('City')
    plt.ylabel('Temperature (°C)')

    # Humidity plot
    plt.subplot(2, 2, 2)
    sns.barplot(x='city', y='humidity', data=weather_df, palette='Blues')
    plt.title('Humidity by City')
    plt.xlabel('City')
    plt.ylabel('Humidity (%)')

    # Wind Speed plot
    plt.subplot(2, 2, 3)
    sns.barplot(x='city', y='wind_speed', data=weather_df, palette='Greens')
    plt.title('Wind Speed by City')
    plt.xlabel('City')
    plt.ylabel('Wind Speed (m/s)')

    # Weather Description plot
    plt.subplot(2, 2, 4)
    sns.countplot(x='description', data=weather_df, order=weather_df['description'].value_counts().index, palette='viridis')
    plt.title('Weather Description Count')
    plt.xlabel('Description')
    plt.ylabel('Count')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

# Call the function to generate Seaborn visualizations
seaborn_visualizations(weather_df)
