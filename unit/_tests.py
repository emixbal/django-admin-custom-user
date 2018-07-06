from django.test import TestCase
from rest_framework.test import APIClient
import json
from django.test.client import ClientHandler

# from .models import Unit
from .tests_data import TestData

class SessionHandler(ClientHandler):
    def get_response(self, request):
        response = super(SessionHandler, self).get_response(request)
        # response.session = request.session.copy()
        response.session = request.session.get('company_id')
        return response

    # def test_post_unit(self):


class SessionTestCase(TestCase):
    def _pre_setup(self):
        super(SessionTestCase, self)._pre_setup()
        self.client.handler = SessionHandler()

        print(self.client.handler)

class UnitTest(SessionTestCase):
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

        self.client.handler = SessionHandler()

    def test_post_unit(self):
        result = self.client.post('/api/unit/', TestData.unit)
        self.assertIsNotNone(result.data) # is method correct?
        # asserting response code with with coorect response code
        self.assertEqual(result.status_code, 201)

    # def test_session_exists(self):
    #     resp = self.client.get("/")
    #     self.assert_(hasattr(resp, "session"))
    #     self.assert_("my_session_key" in resp.session)
    #     self.assertEqual(resp.session["my_session_key"], "Hello world!")
