import unittest
from myflaskapp.app import create_app
from myflaskapp.database import db as _db
from myflaskapp.settings import TestConfig, TestServerNameConfig

from .factories import UserFactory
from .conftest import app
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
        pass
        response = self.client.get(url_for('public.home'))
    #     self.assertTrue('Stranger' in response.get_data(as_text=True))
