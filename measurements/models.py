import os
import requests
from django.db import models
from datetime import datetime

TOKEN = 'c9a3d9450858418edd708a73d631cb4b'
API_URL = 'http://api.openweathermap.org/data/2.5/find?appid={}'.fomrat(TOKEN)

class Measurement(models.Model):
    collection_time = models.DateTimeField(default=datetime.now)
    temperature = models.FloatField(default=0.0)
    temperature_min = models.FloatField(default=0.0)
    temperature_max = models.FloatField(default=0.0)
    wind_velocity = models.FloatField(default=0.0)
    rain_precipitation = models.FloatField(default=0.0,null=True)
    location = models.CharField(max_length=50)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def save_measurements(self, values, latitude, longitude):
        measurement = Measurement()
        response = this.get_specific_data(latitude, longitude)

        measurement.collection_time = response['dt']

        measurement.temperature = response['main']['temp']
        measurement.temperature_min = response['main']['temp_min']
        measurement.temperature_max = response['main']['temp_max']
        measurement.wind_velocity = response['wind']['speed']
        measurement.latitude = response['coord']['lat']
        measurement.longitude = response['coord']['lon']
        measurement.location = response['name']

        measurement.rain_precipitation = response['rain']['1h']

    def get_specific_data(self, latitude, longitude):
        location = '&lat={}&lon={}'.format(latitude, longitude)

        response = requests.get(API_URL + location)

        return response
