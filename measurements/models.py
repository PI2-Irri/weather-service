from django.db import models
from django.utils.timezone import datetime

from locations.models import Location

class Measurement(models.Model):
    collection_time = models.DateTimeField(default=datetime.now)
    temperature = models.FloatField(default=0.0)
    temperature_min = models.FloatField(default=0.0)
    temperature_max = models.FloatField(default=0.0)
    wind_velocity = models.FloatField(default=0.0)
    rain_precipitation = models.FloatField(default=0.0,null=True, blank=True)

    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def transform_data(self, data_integer):
        data = datetime.fromtimestamp(data_integer)
        return data

class MinutelyMeasurement(Measurement):
    def save_measurements(self, location, response):
        measurement = MinutelyMeasurement()
        measurement.collection_time = self.transform_data(response['dt'])

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

        measurement.save()

class ForecastMeasurement(Measurement):
    def save_measurements(self, location, response):
        for data in response:
            measurement = ForecastMeasurement()
            measurement.collection_time = self.transform_data(data['dt'])

            measurement.temperature = data['main']['temp']
            measurement.temperature_min = data['main']['temp_min']
            measurement.temperature_max = data['main']['temp_max']
            measurement.wind_velocity = data['wind']['speed']

            try:
                measurement.latitude = data['coord']['lat']
                measurement.longitude = data['coord']['lon']
            except Exception as exception:
                measurement.latitude = location.latitude
                measurement.longitude = location.longitude

            measurement.location = location

            try:
                measurement.rain_precipitation = data['rain']['3h']
            except Exception as exception:
                measurement.rain_precipitation = None

            measurement.save()
