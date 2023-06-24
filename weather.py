import requests
import json
import argparse

API_KEY = '038d889f3e3a61330a569a10e6297813'

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    #print(data)
    return data

def parse_weather(data):
    try:
        temperature = data['main']['temp']
        temperature -= 273.15
        temperature = round(temperature, 2)
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']
        return temperature, humidity, weather_desc
    except KeyError:
        raise ValueError('Invalid response format from API')

def display_weather(city, temperature, humidity, weather_desc):
    print(f'Weather forecast for {city}:')
    print(f'Temperature: {temperature}°C')
    print(f'Humidity: {humidity}%')
    print(f'Weather description: {weather_desc}')

def main():
    parser = argparse.ArgumentParser(description='Get current weather forecast')
    parser.add_argument('city', metavar='CITY', type=str, help='City name')
    args = parser.parse_args()

    try:
        weather_data = get_weather(args.city)
        temperature, humidity, weather_desc = parse_weather(weather_data)
        display_weather(args.city, temperature, humidity, weather_desc)
    except requests.exceptions.RequestException as e:
        print(f'Error occurred while fetching weather data: {e}')
    except (ValueError, KeyError) as e:
        print(f'Error occurred while parsing weather data: {e}')

if __name__ == '__main__':
    main()