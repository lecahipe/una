import csv
import datetime

from rest_framework import viewsets, views, status
from rest_framework.response import Response

from api import serializers
from api.filters import UserDeviceMetabolicDataDatesFilter
from data.models import UserDeviceMetabolicData
from api.utils import ExportClass


class UserDeviceGlucoseDataView(viewsets.ReadOnlyModelViewSet):
    '''
        View to list all glucose data for all users or retrieve a single user's data
    '''
    queryset = UserDeviceMetabolicData.objects.all()
    serializer_class = serializers.UserDeviceMetabolicDataSerializer
    lookup_field = 'user_id'
    filterset_class = UserDeviceMetabolicDataDatesFilter
    ordering_fields = ['device_timestamp']
    filterset_fields = ['user_id']
    
    def retrieve(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        queryset = self.filter_queryset(self.get_queryset().filter(user_id=user_id))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class CSVUploadView(views.APIView):
    '''
        Upload a CSV file and save the data to the database
    '''
    serializer_class = serializers.CSVUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = serializers.CSVUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = request.FILES['file']
            user_id = file.name.split('.')[0]
            file_data = file.read().decode('utf-8').splitlines()[3:]
            reader = csv.reader(file_data, delimiter=",")
            for row in reader:
                # Create a new record in the database
                UserDeviceMetabolicData.objects.create(
                    user_id = user_id,
                    device = row[0],
                    device_serialnumber = row[1],
                    device_timestamp = datetime.datetime.strptime(row[2], "%d-%m-%Y %H:%M"),
                    recording_type = row[3],
                    glucose_value_history = row[4] or None,
                    glucose_scan = row[5] or None,
                    non_numeric_rapid_acting_insulin = row[6] or None,
                    fast_acting_insulin_units = row[7] or None,
                    non_numeric_food_data = row[8] or None,
                    carbohydrates_grams = row[9] or None,
                    carbohydrates_servings = row[10] or None,
                    non_numeric_depot_insulin = row[11] or None,
                    depot_insulin_units = row[12] or None,
                    notes = row[13] or None,
                    glucose_test_strips = row[14] or None,
                    ketone_mmol = row[15] or None,
                    meal_insulin_units = row[16] or None,
                    correction_insulin_units = row[17] or None,
                    insulin_change_by_user_units = row[18] or None)
                
            return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ExportDataView(views.APIView, ExportClass):
    '''
        Export data in either CSV or JSON format
    '''
    def get(self, request, *args, **kwargs):
        serializer = serializers.ExportDataRequestSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        queryset = UserDeviceMetabolicData.objects.all()
        data = serializers.UserDeviceMetabolicDataSerializer(queryset, many=True).data

        filetype = serializer.validated_data['filetype'].lower()
        if filetype == 'csv':
            return self.export_csv(data)
        elif filetype == 'json':
            return self.export_json(data)
        else:
            return Response({"error": "Invalid filetype"}, status=status.HTTP_400_BAD_REQUEST)
