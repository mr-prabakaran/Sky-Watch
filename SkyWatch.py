from dotenv import load_dotenv
import os
import requests

load_dotenv('.env')
API_KEY = os.getenv('API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        'q':city_name,
        'appid':API_KEY,
        'units':'metric'
    }

    r = requests.get(BASE_URL,params=params)

    if r.status_code == 200:
        data = r.json()
        main = data['main']
        wind = data['wind']
        weather_description = data['weather'][0]['description']

        print(f'City : {city_name}')
        print(f'Temperature : {main['temp']}°C')         #alt + 0176
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Wind Speed: {wind['speed']} m/s")
        print(f"Weather: {weather_description}")
        # print(r.url)
    else:
        print("City not found, please check the city name.")

city = input('Enter city name :')
get_weather(city)