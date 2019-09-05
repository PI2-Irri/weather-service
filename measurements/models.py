from django.db import models
from datetime import datetime


class Measurements(models.Model):
    collection_time = models.DateTimeField(default=datetime.now)
    temperature = models.FloatField(default=0.0)
    temperature_min = models.FloatField(default=0.0)
    temperature_max = models.FloatField(default=0.0)
    wind_velocity = models.FloatField(default=0.0)
    rain_precipitation = models.FloatField(default=0.0)
    location = models.CharField(max_length=50)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
