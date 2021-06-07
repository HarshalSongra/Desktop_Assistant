import requests

class WeatherService(object):
    API_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric";

    API_KEY = "c71eeb32d829e370521a138a908dd48a"

    def __init__(self):
        pass

    def get_weather_data(self, city_name):
        try:
            r = requests.get(WeatherService.API_URL.format(city_name, WeatherService.API_KEY))

            weather_data = (r.json())

            temp = self._extract_temp(weather_data)

            description = self._extract_desc(weather_data)

            return f"Currently, in {city_name}, its {temp} degrees with {description}"

        except Exception as e:
            return 'none'

    def _extract_temp(self, weatherdata):
        temp = weatherdata['main']['temp']

        return temp

    def _extract_desc(self, weatherdata):

        return weatherdata['weather'][0]['description']
