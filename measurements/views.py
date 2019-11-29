from rest_framework import viewsets, mixins
from .models import MinutelyMeasurement
from .models import ForecastMeasurement
from .models import Location
from .serializers import MinutelyMeasurementSerializer
from .serializers import ForecastMeasurementSerializer
from rest_framework.exceptions import APIException


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
                location = self.queryset.get(
                    location_name=location_name
                )
            except Exception as exception:
                try:
                    location = self.queryset.get(
                        latitude=float("{0:.2f}".format(latitude)),
                        longitude=float("{0:.2f}".format(longitude))
                    )
                except Exception as exception:
                    raise APIException(
                        {'error': 'Location not valid.'}
                    )

        if location is not None:
            self.queryset = self.queryset.filter(location=location)

        if start_date and end_date:
            self.queryset = self.queryset.filter(
                collection_time__gte=start_date,
                collection_time__lte=end_date
            )
            for q in self.queryset:
                print(q.__dict__)

        if self.option == 'minutely':
            if self.queryset.last():
                return [self.queryset.last()]
            else:
                return []
        else:
            return self.queryset.reverse()


class MinutelyMeasurementViewSet(MeasurementViewSet):
    queryset = MinutelyMeasurement.objects.select_related('location').all().order_by('id')
    serializer_class = MinutelyMeasurementSerializer
    option = 'minutely'

class ForecastMeasurementViewSet(MeasurementViewSet):
    queryset = ForecastMeasurement.objects.select_related('location').all().order_by('id')
    serializer_class = ForecastMeasurementSerializer
    option = 'forecast'
