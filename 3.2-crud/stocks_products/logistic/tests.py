from unittest import TestCase

from rest_framework.test import APIClient


class Test1(TestCase):
    def test_simple(self):
        client = APIClient()
        url = '/api/v1/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
