from unittest import TestCase
from fastapi.testclient import TestClient
from salary_calc_fastapi.app import app


class TestHellowWorldEndpoint(TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_successful_response(self):
        response = self.client.get('/helloworld')
        expected_response = {"hello": "world"}

        self.assertEqual(expected_response, response.json())
