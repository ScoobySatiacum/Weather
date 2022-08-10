import requests

from config import Config
from weather_data import WeatherData

class Weather:

    def __init__(self):
        self.api_key = Config.API_KEY

    def get_weather_data(self, lat, lon, test=False):
        if test:
            text = ''
            with open(r'C:\Users\skyle\Documents\dev\python\Weather\test_data\test_data.json') as fo:
                text = fo.read()
            wd = WeatherData(text)
            return wd
        else:
            base_url = 'http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&units=imperial'
            url = base_url.format(lat, lon, self.api_key)
            r = requests.get(url)
            if r.status_code == 200:
                wd = WeatherData(r.text)
                with open(r'C:\Users\skyle\Documents\dev\python\Weather\test_data\test_data.json', 'w') as fo:
                    fo.writelines(r.text)
                return wd
            else:
                return None          