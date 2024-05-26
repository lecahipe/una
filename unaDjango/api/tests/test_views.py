import pytest
from rest_framework.test import APIClient
from api.factories import UserDeviceMetabolicDataFactory
from django.urls import reverse

from data.models import UserDeviceMetabolicData

@pytest.mark.django_db
class TestUserDeviceMetabolicDataView:
    '''
        Test the UserDeviceMetabolicDataView view
    '''
    def setup_method(self):
        self.client = APIClient()
        self.url = reverse('userdevicemetabolicdata-list')
        self.data_count = 4
        self.page_size = 4
        self.data = UserDeviceMetabolicDataFactory.create_batch(self.data_count)

    def test_list_view(self):
        '''
            Test that the view can list all records
        '''
        response = self.client.get(self.url)
        assert response.status_code == 200 # tests that the response status code is 200
        assert len(response.json()) == self.data_count # tests that the number of records returned is equal to the number of records created
        assert len(response.data['results']) == self.page_size # tests that the page size is 5
        assert 'next' in response.data # tests that there is a next page in the response
        assert response.data['previous'] is None # tests that there is no previous page in the response

    def test_list_view_user(self):
        '''
            Test that the view can list by user_id in the query parameters
        '''
        user_id = self.data[0].user_id
        response = self.client.get(self.url+user_id+'/')
        assert response.status_code == 200 # tests that the response status code is 200
        data = response.json()
        assert all(i['user_id'] == user_id for i in data) # tests that all records returned have the same user_id

    def test_filter_by_user_id(self):
        ''' 
            Test that the view can filter records by user_id, all records returned should have the same user_id
        '''
        user_id = self.data[0].user_id
        response = self.client.get(self.url, {'user_id': user_id})
        assert response.status_code == 200  # tests that the response status code is 200
        data = response.json()
        assert all(i['user_id'] == user_id for i in data['results']) # tests that all records returned have the same user_id
        


@pytest.mark.django_db
class TestCSVUploadView:
    '''
        Test the CSVUploadView view
    '''
    def setup_method(self):
        self.client = APIClient()
        self.url = reverse('upload-csv')
        self.data_count = 4
        self.data = UserDeviceMetabolicDataFactory.create_batch(self.data_count)
        self.user_id = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'
    
    def test_upload_view(self):
        '''
            Test that the view can upload a CSV file and save the data to the database
        '''
        # using small file for testing copied from data sample
        data = {
            'file': open(f'api/tests/files/{self.user_id}.csv', 'rb')
        }
        
        response = self.client.post(self.url, data, format='multipart')
        assert response.status_code == 201
        # check if data was created for user_id
        assert UserDeviceMetabolicData.objects.filter(user_id=self.user_id).exists() == True
    
    