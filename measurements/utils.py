import os
import requests
from .models import Measurement
from locations.models import Location

TOKEN = os.getenv('TOKEN', '')
API_URL = os.getenv('API_URL', '')

class DataCollector():
    def get_specific_data(self, latitude, longitude):
        location = '&lat={}&lon={}'.format(latitude, longitude)
        response = requests.get(API_URL + TOKEN + location).json()
        return response['list'][0]

    def save_data(self, location):
        response = this.get_specific_data(
            location.latitude,
            location.longitude
        )
        measurement = Measurement()
        measurement.save_measurements(location, response)

    def collect_measurements(self):
        locations = Location.objects.all()

        for location in locations:
            this.save_data(location)
