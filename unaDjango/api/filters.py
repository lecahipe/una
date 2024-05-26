import django_filters
from data.models import UserDeviceMetabolicData

class UserDeviceMetabolicDataDatesFilter(django_filters.FilterSet):
    start = django_filters.DateFilter(field_name='device_timestamp', lookup_expr='gt')  # Greater than
    stop = django_filters.DateFilter(field_name='device_timestamp', lookup_expr='lt')  # Less than
    user_id = django_filters.CharFilter(field_name='user_id', lookup_expr='exact')
    class Meta:
        model = UserDeviceMetabolicData
        fields = ['start', 'stop', 'user_id']