# WeatherAI

Weather forecasting using GitHub Copilot and OpenWeather API in CLI.
Also get AI suggesstions for your Outfit based on weather forecast. Like -
- Dont forget to wear your Sunglasses!
- Avoid going out today, its too cold!
- Its raining today, dont forget to carry your umbrella!
- Its too hot today, dont forget to carry your water bottle!
- The weather is perfect today, enjoy your day!



### Demo

![](https://github.com/Fastest-Coder-First/Weather_Forecast/blob/main/Output_Screenshot.jpeg)

## My Experience with GitHub Copilot:
Genuinley speaking, I was not expecting this much accuracy from GitHub Copilot. It is really good, really impressed by it. I'm sure it will be a great helping tool for developers.

when a prompt is given in form of comment, copilot writes most of the code itself. 

It even helped me secure my API key by suggesting me to use environment variables.

- It suggested to use argparse for command line arguments.
- It helped write Quality code.
- It aided in writing error handling code.
- Development Time was significantly reduced, Now that's some serious SPEED.



### Architecture
![](https://github.com/Fastest-Coder-First/Weather_Forecast/blob/main/Architecture.jpeg)



### Installation


This project files requires [**Python 3**](https://www.python.org/downloads/) and the following Python libraries installed:

- [OpenWeather API](https://openweathermap.org/api)
- openai 
- requests
- json
- argparse


### Add libraries

```bash
pip install -r requirements.txt
```  

### Get OpenAI API Key :
https://platform.openai.com/account/api-keys \
Replace < YOUR API KEY HERE> in code with this Key 


### Run
To view Minimal Weather Forecast from terminal, go to the project loc in cmd and paste this:

```bash
python weather.py <city_name>
```  

### Run
To also get AI suggesstions, go to the integrated terminal and paste this:

```bash
python weatherAI.py Hyderabad Goa
```  

#### Example Command
```bash
python weatherAI.py Goa
```