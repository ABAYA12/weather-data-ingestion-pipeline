import requests
from datetime import datetime
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
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
        return None

api_key = '163ad7c99574a44a2b89c05e302393b7'
cities = ["ACCRA", "KUMASI", "SEKONDI-TAKORADI", "CAPE COAST", "TAMALE",
          "SUNYANI", "BOLGATANGA", "WA", "HO", "KOFORIDUA", "TEMA", "TARKWA"]

weather_data_list = []
for city in cities:
    weather_data = get_weather(api_key, city)
    if weather_data:
        weather_data_list.append(weather_data)

weather_df = pd.DataFrame(weather_data_list)

if not weather_df.empty:
    weather_df.to_csv('weather_data.csv', index=False)
else:
    print("No weather data available.")

def plot_visualizations(weather_df):
    if not weather_df.empty:
        # Plotly Interactive Visualizations
        fig_temp = px.bar(weather_df, x='city', y='temperature', title='Temperature by City',
                          labels={'temperature': 'Temperature (°C)'},
                          hover_data={'temperature': ':.2f°C'})
        fig_temp.update_traces(marker_color='skyblue')
        fig_temp.update_layout(xaxis_title='City', yaxis_title='Temperature (°C)')

        fig_humidity = px.bar(weather_df, x='city', y='humidity', title='Humidity by City',
                              labels={'humidity': 'Humidity (%)'},
                              hover_data={'humidity': ':.2f%'})
        fig_humidity.update_traces(marker_color='lightgreen')
        fig_humidity.update_layout(xaxis_title='City', yaxis_title='Humidity (%)')

        fig_wind = px.bar(weather_df, x='city', y='wind_speed', title='Wind Speed by City',
                          labels={'wind_speed': 'Wind Speed (m/s)'},
                          hover_data={'wind_speed': ':.2f m/s'})
        fig_wind.update_traces(marker_color='lightcoral')
        fig_wind.update_layout(xaxis_title='City', yaxis_title='Wind Speed (m/s)')

        fig_description = px.histogram(weather_df, x='description', title='Weather Description Count',
                                        labels={'description': 'Description', 'count': 'Count'},
                                        category_orders={"description": weather_df['description'].value_counts().index})
        fig_description.update_traces(marker_color='orange')
        fig_description.update_layout(xaxis_title='Description', yaxis_title='Count')

        fig_temp.show()
        fig_humidity.show()
        fig_wind.show()
        fig_description.show()
    else:
        print("No weather data available.")

def seaborn_visualizations(weather_df):
    if not weather_df.empty:
        plt.figure(figsize=(14, 8))

        plt.subplot(2, 2, 1)
        sns.barplot(x='city', y='temperature', data=weather_df, palette='coolwarm')
        plt.title('Temperature by City')
        plt.xlabel('City')
        plt.ylabel('Temperature (°C)')
        plt.xticks(rotation=45)

        plt.subplot(2, 2, 2)
        sns.barplot(x='city', y='humidity', data=weather_df, palette='Blues')
        plt.title('Humidity by City')
        plt.xlabel('City')
        plt.ylabel('Humidity (%)')
        plt.xticks(rotation=45)

        plt.subplot(2, 2, 3)
        sns.barplot(x='city', y='wind_speed', data=weather_df, palette='Greens')
        plt.title('Wind Speed by City')
        plt.xlabel('City')
        plt.ylabel('Wind Speed (m/s)')
        plt.xticks(rotation=45)

        plt.subplot(2, 2, 4)
        sns.countplot(x='description', data=weather_df, order=weather_df['description'].value_counts().index, palette='viridis')
        plt.title('Weather Description Count')
        plt.xlabel('Description')
        plt.ylabel('Count')
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()
    else:
        print("No weather data available.")

plot_visualizations(weather_df)
seaborn_visualizations(weather_df)
