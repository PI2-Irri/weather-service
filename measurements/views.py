from rest_framework import viewsets
from .models import Measurement
from .models import Location
from .serializers import MeasurementSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.select_related('location').all()
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        location_name = self.request.query_params.get('location', None)
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if location_name is not None:
            try:
                location = self.queryset.filter(
                    location_name=location_name,
                    latitude=float("{0:.2f}".format(latitude)),
                    longitude=float("{0:.2f}".format(longitude))
                )
            except Exception as exception:
                location = None

        if location is not None:
            self.queryset = self.queryset.filter(location=location)

        if start_date is not None and end_date is not None:
            pass


        return self.queryset
