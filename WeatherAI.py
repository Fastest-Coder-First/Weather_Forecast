'''
Github Copilot helped to handle the exceptions and errors in the code,
improved the code quality and also helps to write the code faster.
Copilot also improved readability of the code.


'''

import openai
import requests
import json
import argparse

MEGENTA = '\033[35m'
ORANGE = '\033[38;5;208m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
END_COLOR = '\033[0m'

openai.api_key = "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"
API_KEY = '038d889f3e3a61330a569a10e6297813'

def chat_query(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

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
    print(MEGENTA+ f'\nWeather forecast for {city}:'+ END_COLOR)
    print(RED + f'Temperature: {temperature}°C' + END_COLOR)
    print(BLUE + f'Humidity: {humidity}%'+ END_COLOR)
    print(GREEN + f'Weather description: {weather_desc}'+ END_COLOR)

def main():
    parser = argparse.ArgumentParser(description='Get current weather forecast')
    parser.add_argument('cities', metavar='CITY', type=str, nargs='+', help='City name(s)')
    args = parser.parse_args()

    for city in args.cities:
        try:
            weather_data = get_weather(city)
            temperature, humidity, weather_desc = parse_weather(weather_data)
            display_weather(city, temperature, humidity, weather_desc)

            prompt = f"What's the weather like in {city}? and which dressing style would be good for it? give any suggestions like wear sunglasses, umbrella, sunscreen, avoid going out, etc or anything in detailed"
            response = chat_query(prompt)
            print(ORANGE + "AI Assisstant: "+ END_COLOR + f"{response}" )
            
        except requests.exceptions.RequestException as e:
            print(f'Error occurred while fetching weather data for {city}: {e}')
        except (ValueError, KeyError) as e:
            print(f'Error occurred while parsing weather data for {city}: {e}')

if __name__ == '__main__':
    main()


