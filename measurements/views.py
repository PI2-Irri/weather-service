from rest_framework import viewsets, mixins
from .models import MinutelyMeasurement
from .models import ForecastMeasurement
from .models import Location
from .serializers import MinutelyMeasurementSerializer
from .serializers import ForecastMeasurementSerializer


class MeasurementViewSet(mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = None

    def get_queryset(self):
        location_name = self.request.query_params.get('location', None)
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        location = None

        if location_name is not None:
            try:
                location = self.queryset.filter(
                    location_name=location_name,
                    latitude=float("{0:.2f}".format(latitude)),
                    longitude=float("{0:.2f}".format(longitude))
                )
            except Exception as exception:
                print(exception)

        if location is not None:
            self.queryset = self.queryset.filter(location=location)

        if start_date is not None and end_date is not None:
            self.queryset = self.queryset.filter(
                collection_time__gte=start_date
            )
            self.queryset = self.queryset.filter(
                collection_time__lte=end_date
            )

        return self.queryset.reverse()


class MinutelyMeasurementViewSet(MeasurementViewSet):
    queryset = MinutelyMeasurement.objects.select_related('location').all().order_by('id')
    serializer_class = MinutelyMeasurementSerializer


class ForecastMeasurementViewSet(MeasurementViewSet):
    queryset = ForecastMeasurement.objects.select_related('location').all().order_by('id')
    serializer_class = ForecastMeasurementSerializer
