from rest_framework import serializers
from data.models import UserDeviceMetabolicData


class UserDeviceMetabolicDataSerializer(serializers.ModelSerializer):
    '''
        Serialize the UserDeviceMetabolicData model
    '''
    class Meta:
        model = UserDeviceMetabolicData
        fields = '__all__'


class CSVUploadSerializer(serializers.Serializer):
    '''
        Serialize the CSV file
    '''
    file = serializers.FileField()
