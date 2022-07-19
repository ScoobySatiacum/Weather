import requests

from config import Config

class Weather:

    def __init__(self):
        self.api_key = Config.API_KEY

    def get_weather_data(self, lat, lon):
        base_url = 'http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&units=imperial'