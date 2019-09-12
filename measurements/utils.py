import os
import requests
from .models import Measurement

TOKEN = os.getenv('TOKEN', '')
API_URL = os.getenv('API_URL', '')

class DataCollector():
    def get_specific_data(self, latitude, longitude):
        location = '&lat={}&lon={}'.format(latitude, longitude)
        response = requests.get(API_URL + TOKEN + location).json()
        return response['list'][0]

    def save_data(self, latitude, longitude):
        response = this.get_specific_data(latitude, longitude)
        measurement = Measurement()
        measurement.save_measurements(response)
