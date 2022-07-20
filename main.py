from geo import Geo
from weather import Weather

def main():
    g = Geo()
    geo = g.search_for_location('Covington, WA')
    if geo:
        w = Weather()
        wd = w.get_weather_data(geo.lat, geo.lon)
        if wd:
            print(wd.current.temp)


if __name__ == '__main__':
    main()