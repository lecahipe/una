from rest_framework import viewsets

from api import serializers
from api.filters import UserDeviceMetabolicDataDatesFilter
from data.models import UserDeviceMetabolicData


class UserDeviceGlucoseDataView(viewsets.ReadOnlyModelViewSet):
    '''
        View to list all glucose data for all users or retrieve a single user's data
    '''
    queryset = UserDeviceMetabolicData.objects.all()
    serializer_class = serializers.UserDeviceMetabolicDataSerializer
    lookup_field = 'user_id'
    filterset_class = UserDeviceMetabolicDataDatesFilter
    