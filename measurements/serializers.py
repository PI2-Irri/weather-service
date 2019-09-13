from rest_framework import serializers
from .models import Measurement


class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurement
        fields = (
            'id',
            'collection_time',
            'temperature',
            'temperature_min',
            'temperature_max',
            'wind_velocity',
            'rain_precipitation',
            'location',
            'url'
        )
