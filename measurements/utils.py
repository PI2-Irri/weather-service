import os
import requests
from .models import MinutelyMeasurement
from .models import ForecastMeasurement
from locations.models import Location

TOKEN = os.getenv('TOKEN_ID', '')
API_URL = os.getenv('API_URL', '')
FORECAST_URL = os.getenv('FORECAST_URL', '')

class DataCollector():
    def get_specific_data(self, location_name, latitude, longitude, url):
        if latitude and longitude:
            location = '&lat={}&lon={}'.format(latitude, longitude)
        else:
            location = '&q=' + location_name + ',br'

        response = requests.get(url + '?appid=' + TOKEN + location + '&units=metric').json()
        print("Get specific data: {}".format(url + '?appid=' + TOKEN + location))
        return response['list']

    def save_minutelly_data(self, location):
        response = self.get_specific_data(
            location.location_name,
            location.latitude,
            location.longitude,
            API_URL
        )
        measurement = MinutelyMeasurement()
        measurement.save_measurements(location, response[0])

    def save_forecast_data(self, location):
        response = self.get_specific_data(
            location.location_name,
            location.latitude,
            location.longitude,
            FORECAST_URL
        )
        measurement = ForecastMeasurement()
        measurement.save_measurements(location, response[0:7])

    def collect_minutely_measurements(self):
        locations = Location.objects.all()

        for location in locations:
            self.save_minutelly_data(location)

    def collect_forecast_measurements(self):
        locations = Location.objects.all()

        for location in locations:
            self.save_forecast_data(location)
