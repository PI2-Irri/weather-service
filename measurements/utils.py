import os
import requests
from .models import Measurement

TOKEN = 'c9a3d9450858418edd708a73d631cb4b'
API_URL = 'http://api.openweathermap.org/data/2.5/find?appid={}'.format(TOKEN)

class DataCollector():
    def get_specific_data(self, latitude, longitude):
        location = '&lat={}&lon={}'.format(latitude, longitude)
        response = requests.get(API_URL + location).json()
        return response['list']

    def save_data(self, latitude, longitude):
        response = this.get_specific_data(latitude, longitude)
        measurement = Measurement()
        measurement.save_measurements(response)
