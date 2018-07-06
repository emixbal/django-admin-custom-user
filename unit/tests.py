from django.test import TestCase
from rest_framework.test import APIClient
import json
from django.test.client import ClientHandler

# from .models import Unit
from .tests_data import TestData

# Create your tests here.
class UnitTest(TestCase):
    def setUp(self):
        user_data = {
            'email': 'admin@gmail.com',
            'username': 'admin',
            'password': 'admin123',
        }
        user = self.client.post('/api/user/', user_data)
        auth = self.client.post('/api/authentication/', user_data)
        headers = {
            'HTTP_AUTHORIZATION': 'JWT '+ auth.data['token']
        }
        self.client = APIClient()
        self.client.credentials(**headers) # make all fuctions authorized

        # run populate function
        self.populate()

    # populating database
    def populate(self):
        # create company
        company=self.client.post('/api/companies/', TestData.company).data

        # use company_id
        use_company=self.client.get('/api/companies/%s/use/' %(company['id']))

        # populate data unit
        unit = self.client.post('/api/unit/', TestData.unit).data

        # save attr id in variable
        self.id = unit['id']

        # save company_id from session
        self.company_id = use_company.data


    def test_get_specific_unit(self):
        result = self.client.get('/api/unit/%s/?company_id=%s' % (self.id, self.company_id))

        self.assertEqual(TestData.unit['name'], result.data['name'])
        self.assertEqual(TestData.unit['code'], result.data['code'])

    def test_post_unit(self):
        result = self.client.post('/api/unit/', TestData.unit)
        self.assertIsNotNone(result.data) # is method correct?
        # asserting response code with with coorect response code
        self.assertEqual(result.status_code, 201)

    def test_get_unit(self):
        result = self.client.get('/api/unit/')
        self.assertIsNotNone(result.data) # is method correct?
        # asserting response code with with coorect response code
        self.assertEqual(result.status_code, 200)

    def test_patch_specific_unit(self):
        unit_updated = self.client.patch('/api/unit/%s/' %(self.id), TestData.new_unit)
        result = self.client.get('/api/unit/%s/?company_id=%s' % (self.id, self.company_id))

        self.assertEqual(TestData.new_unit['name'], result.data['name'])
        self.assertEqual(TestData.new_unit['code'], result.data['code'])

    def test_delete_unit(self):
        # populating data
        unit = self.client.post('/api/unit/', TestData.unit)
        # delete data by id
        delete = self.client.delete('/api/unit/%s/' % (unit.data['id']))
        # checking data by id, is data still exist ?
        result = self.client.get('/api/unit/%s/' % (unit.data['id']))
        self.assertEqual(result.status_code, 404)
