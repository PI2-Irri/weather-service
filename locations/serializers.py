from rest_framework import serializers
from .models import Location
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id',
            'location_name',
            'latitude',
            'longitude',
            'url'
        )
   
    def create(self, validated_data):

        try:
            location = Location.objects.get(location_name=validated_data.get('location_name'))
        except Location.DoesNotExist:

            try:
                location = Location.objects.create(
                    location_name=validated_data.get('location_name'),
                    latitude=validated_data.get('latitude'),
                    longitude=validated_data.get('longitude')
                )
            except Exception:
                raise APIException(
                    {'error': 'Could not register'}
                )

        return location
