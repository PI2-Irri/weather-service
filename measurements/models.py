from django.db import models
from datetime import datetime

from .utils import *
from measurements.models import Location

class Measurement(models.Model):
    collection_time = models.DateTimeField(default=datetime.now)
    temperature = models.FloatField(default=0.0)
    temperature_min = models.FloatField(default=0.0)
    temperature_max = models.FloatField(default=0.0)
    wind_velocity = models.FloatField(default=0.0)
    rain_precipitation = models.FloatField(default=0.0,null=True, blank=True)

    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def save_measurements(self, response):
        location = Location()

        location.location_name = response['name']
        location.latitude = response['coord']['lat']
        location.longitude = response['coord']['lon']

        measurement = Measurement()

        measurement.collection_time = response['dt']

        measurement.temperature = response['main']['temp']
        measurement.temperature_min = response['main']['temp_min']
        measurement.temperature_max = response['main']['temp_max']
        measurement.wind_velocity = response['wind']['speed']
        measurement.latitude = response['coord']['lat']
        measurement.longitude = response['coord']['lon']
        measurement.location = location

        try:
            measurement.rain_precipitation = response['rain']['1h']
        except Exception as exception:
            measurement.rain_precipitation = None
