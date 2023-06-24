# WeatherAI

Weather forecasting using GitHub Copilot and OpenWeather API in CLI

### Demo

![](https://github.com/Fastest-Coder-First/Weather_Forecast/blob/main/ScreenshotOutput.jpeg)

![](https://github.com/Fastest-Coder-First/Weather_Forecast/blob/main/OutputCitiesForecast.jpeg)



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
To run from VSCode's terminal, go to the integrated terminal and paste this:

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