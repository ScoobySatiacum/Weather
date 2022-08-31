import json
import requests

from config import Config

class Geo:

    def __init__(self):
        self.api_key = Config.API_KEY

    def search_for_location_by_city(self, user_location):
        base_url = 'http://api.openweathermap.org/geo/1.0/direct?q={},us&appid={}'
        url = base_url.format(user_location.replace(' ', ''), self.api_key)
        r = requests.get(url)
        if r.status_code == 200:
            geo = CityData(r.text)

            return geo

    def search_for_location_by_zip(self, user_location):
        base_url = 'http://api.openweathermap.org/geo/1.0/zip?zip={},us&appid={}'
        url = base_url.format(user_location.replace(' ', ''), self.api_key)
        r = requests.get(url)
        if r.status_code == 200:
            geo = ZipData(r.text)

            return geo

class CityData:

    def __init__(self, data):
        self.__dict__ = json.loads(data.replace('[','').replace(']', ''))

        self.name = self.__dict__['name']
        self.lat = self.__dict__['lat']
        self.lon = self.__dict__['lon']
        self.country = self.__dict__['country']
        self.state = self.__dict__['state']

class ZipData:

    def __init__(self, data):
        self.__dict__ = json.loads(data.replace('[','').replace(']', ''))

        self.zip = self.__dict__['zip']
        self.name = self.__dict__['name']
        self.lat = self.__dict__['lat']
        self.lon = self.__dict__['lon']
        self.country = self.__dict__['country']

def main():
    g = Geo()
    #geo = g.search_for_location_by_city('Covington, WA')
    geo = g.search_for_location_by_zip('98042')
    print(geo.name)

if __name__ == '__main__': main()