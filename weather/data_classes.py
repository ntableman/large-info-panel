from datetime import datetime
import json
from weather.constants import WeatherCondition


class Weather:
    def __init__(self, inside_data: json , sunrise: float, sunposition: float):
        self.inside_data = inside_data
        #try:
        #    self.condition = WeatherCondition(condition)
        #except ValueError:
        #    self.condition = WeatherCondition.SNOW
        self.sunrise = datetime.fromtimestamp(sunrise)
        self.sunposition = datetime.fromtimestamp(sunposition)

class WeatherData:
    def __init__(self, current: Weather):
        self.current = current
