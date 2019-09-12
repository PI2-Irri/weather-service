from django.db import models
from datetime import datetime

from locations.models import Location

class Measurement(models.Model):
    collection_time = models.DateTimeField(default=datetime.now)
    temperature = models.FloatField(default=0.0)
    temperature_min = models.FloatField(default=0.0)
    temperature_max = models.FloatField(default=0.0)
    wind_velocity = models.FloatField(default=0.0)
    rain_precipitation = models.FloatField(default=0.0,null=True, blank=True)

    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def save_measurements(self, location, response):
        self.collection_time = response['dt']

        self.temperature = response['main']['temp']
        self.temperature_min = response['main']['temp_min']
        self.temperature_max = response['main']['temp_max']
        self.wind_velocity = response['wind']['speed']
        self.latitude = response['coord']['lat']
        self.longitude = response['coord']['lon']
        self.location = location

        try:
            self.rain_precipitation = response['rain']['1h']
        except Exception as exception:
            self.rain_precipitation = None

        self.save()
