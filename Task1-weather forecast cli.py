import requests
import argparse

API_KEY = 'ebe1579a2b2769c3da476b6d8acd91a1'

def get_weather(city_name):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    
    response = requests.get(base_url)
    data = response.json()
    reverse="\033[;7m]"
    if data['cod'] == 200:
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']

        print(f'{reverse}Weather in {city_name}:\n'
                                 f'Temperature: {temperature}°C\n'
                                 f'Weather Description: {weather_description}\n'
                                 f'Humidity: {humidity}%')
    else:
        print('City not found.')
if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="WEATHER FORECAST CLI")
    parser.add_argument("city_name",help="Enter city for which weather to be fetch")
    args=parser.parse_args()
    get_weather("Agra")