from rest_framework import serializers, viewsets, mixins
from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        location_name = self.request.query_params.get('location', None)
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)

        if location_name is not None:
            if latitude is not None and longitude is not None:
                self.queryset = self.queryset.filter(
                    location_name=location_name,
                    latitude=float("{0:.2f}".format(latitude)),
                    longitude=float("{0:.2f}".format(longitude))
                )
            else:
                self.queryset = self.queryset.filter(
                    location_name=location_name
                )

        return self.queryset
