import unittest
from myflaskapp.app import create_app
from myflaskapp.settings import TestConfig, TestServerNameConfig



from flask import url_for

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        """An application for the tests."""
        self.app = create_app(TestServerNameConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get(url_for('public.home'))
        self.assertTrue('To-Do' in response.get_data(as_text=True))
