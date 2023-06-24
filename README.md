# WeatherAI

Weather forecasting using GitHub Copilot and OpenWeather API in CLI.
Also get AI suggesstions for your Outfit based on weather forecast. Like -
- Dont forget to wear your Sunglasses!
- Avoid going out today, its too cold!
- Its raining today, dont forget to carry your umbrella!
- Its too hot today, dont forget to carry your water bottle!
- The weather is perfect today, enjoy your day!



### Demo

![](https://github.com/Fastest-Coder-First/Weather_Forecast/blob/main/Screenshot2.jpeg)

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
python weatherAI.py <city_name>
```  

#### Example Command
```bash
python weatherAI.py Goa
```