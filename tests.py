import os
import unittest
import json

from app import app

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_sum_of_list_of_numbers(self):
        response = self.client.get(
            '/total',
        )
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.data.decode('utf-8'))
        self.assertEqual(res['total'], 50000005000000)
if __name__ == '__main__':
    unittest.main()
