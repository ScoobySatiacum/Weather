import datetime
import json
import os
from PIL import ImageTk, Image
from io import BytesIO
import requests

class WeatherData:

    def __init__(self, data):
        self.__dict__ = json.loads(data)

        self.lat = self.__dict__['lat']
        self.lon = self.__dict__['lon']
        self.timezone = self.__dict__['timezone']
        self.timezone_offset = self.__dict__['timezone_offset']
        self.current = Current(self.__dict__['current'])
        self.hourly_list = []
        for hour in self.__dict__['hourly']:
            self.hourly_list.append(Hourly(hour))
        self.daily_list = []
        for day in self.__dict__['daily']:
            self.daily_list.append(Daily(day))
        self.next_12_hours = []
        self.build_12_hour_list()

    def build_12_hour_list(self):
        hours = 0
        time_now = datetime.datetime.now().timestamp()
        for hour in self.hourly_list:
            if hours < 12:
                if hour.dt > time_now:
                    self.next_12_hours.append(hour)
                    hours += 1

class Current:

    def __init__(self, data):

        self.dt = data['dt']
        self.sunrise = data['sunrise']
        self.sunset = data['sunset']
        self.temp = data['temp']
        self.feels_like = data['feels_like']
        self.pressure = data['pressure']
        self.humidity = data['humidity']
        self.dew_point = data['dew_point']
        self.clouds = data['clouds']
        self.uvi = data['uvi']
        self.visibility = data['visibility']
        self.wind_speed = data['wind_speed']
        self.wind_deg = data['wind_deg']
        self.weather = CurrentWeather(data['weather'])

        self.weather.retrieve_current_weather_icons()

class CurrentWeather:

    def __init__(self, data):

        self.id = data[0]['id']
        self.main = data[0]['main']
        self.description = data[0]['description']
        self.icon = data[0]['icon']
        self.image_raw_data = None
        self.image = None

    def retrieve_current_weather_icons(self):
        base_url = 'http://openweathermap.org/img/wn/{}.png'
        # retrieve icons for current weather object
        filename = self.icon + '.png'
        working_dir = os.path.dirname(os.path.realpath(__file__))
        image_dir = os.path.join(working_dir, 'icons')

        if not os.path.exists(image_dir):
            os.mkdir(image_dir)

        if not os.path.exists(os.path.join(image_dir, filename)):
            current_weather_url = base_url.format(self.icon)
            r = requests.get(current_weather_url)
            if r.status_code == 200:
                self.image_raw_data = r.content
                self.image = ImageTk.PhotoImage(Image.open(BytesIO(self.image_raw_data)))
                icon = Image.open(BytesIO(self.image_raw_data))
                icon.save(os.path.join(image_dir, filename))
        else:
            self.image = ImageTk.PhotoImage(Image.open(os.path.join(image_dir, filename)))

class Hourly():

    def __init__(self, data):

        self.dt = data['dt']
        self.time_only = datetime.datetime.fromtimestamp(self.dt).strftime('%H:%M')
        self.temp = data['temp']
        self.feels_like = data['feels_like']
        self.pressure = data['pressure']
        self.humidity = data['humidity']
        self.dew_point = data['dew_point']
        self.clouds = data['clouds']
        self.uvi = data['uvi']
        self.visibility = data['visibility']
        self.wind_speed = data['wind_speed']
        self.wind_deg = data['wind_deg']
        self.weather = CurrentWeather(data['weather'])
        self.pop = data['pop']

        self.weather.retrieve_current_weather_icons()

class Daily:

    def __init__(self, data):

        self.dt = data['dt']
        self.date = datetime.datetime.fromtimestamp(self.dt).strftime('%m/%d/%y')
        self.sunrise = data['sunrise']
        self.sunset = data['sunset']
        self.moonrise = data['moonrise']
        self.moonset = data['moonset']
        self.moon_phase = data['moon_phase']
        self.moon_phase_name = None
        self.temp = DailyTemp(data['temp'])
        self.feels_like = DailyFeelsLike(data['feels_like'])
        self.pressure = data['pressure']
        self.humidity = data['humidity']
        self.dew_point = data['dew_point']
        self.clouds = data['clouds']
        self.uvi = data['uvi']
        self.wind_speed = data['wind_speed']
        self.wind_gust = data['wind_gust']
        self.wind_deg = data['wind_deg']
        self.pop = data['pop']
        self.weather = CurrentWeather(data['weather'])

        self.calculate_moon_phase()
        self.weather.retrieve_current_weather_icons()

    def calculate_moon_phase(self):
        if self.moon_phase == 0 or self.moon_phase == 1:
            self.moon_phase_name = 'new moon'
        elif self.moon_phase == 0.25:
            self.moon_phase_name = 'first quarter moon'
        elif self.moon_phase == 0.5:
            self.moon_phase_name = 'full moon'
        elif self.moon_phase == 0.75:
            self.moon_phase_name = 'last quarter moon'

class DailyTemp:

    def __init__(self, data):

        self.morn = data['morn']
        self.day = data['day']
        self.eve = data['eve']
        self.night = data['night']
        self.min = data['min']
        self.max = data['max']

class DailyFeelsLike:

    def __init__(self, data):

        self.morn = data['morn']
        self.day = data['day']
        self.eve = data['eve']
        self.night = data['night']