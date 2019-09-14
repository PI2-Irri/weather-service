import os
import requests
from .models import Measurement
from locations.models import Location

TOKEN = os.getenv('TOKEN_ID', '')
API_URL = os.getenv('API_URL', '')

class DataCollector():
    def get_specific_data(self, latitude, longitude):
        location = '&lat={}&lon={}'.format(latitude, longitude)
        response = requests.get(API_URL + TOKEN + location).json()
        print("Get specific data: {}".format(API_URL + TOKEN + location))
        return response['list'][0]

    def save_data(self, location):
        print("Save data")
        response = self.get_specific_data(
            location.latitude,
            location.longitude
        )
        measurement = Measurement()
        measurement.save_measurements(location, response)

    def collect_minutely_measurements(self):
        locations = Location.objects.all()

        for location in locations:
            self.save_data(location)
