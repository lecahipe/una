import pytest
from rest_framework.test import APIClient
from api.factories import UserDeviceMetabolicDataFactory
from django.urls import reverse

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

    def test_filter_by_user_id(self):
        ''' 
            Test that the view can filter records by user_id, all records returned should have the same user_id
        '''
        user_id = self.data[0].user_id
        response = self.client.get(self.url, {'user_id': user_id})
        assert response.status_code == 200  # tests that the response status code is 200
        data = response.json()
        assert all(i['user_id'] == user_id for i in data['results']) # tests that all records returned have the same user_id