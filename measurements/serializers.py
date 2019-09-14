from rest_framework import serializers
from .models import MinutelyMeasurement
from .models import ForecastMeasurement


class MinutelyMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutelyMeasurement
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


class ForecastMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ForecastMeasurement
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
