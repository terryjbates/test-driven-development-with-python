from flask import Flask
from flask_testing import LiveServerTestCase
from myflaskapp.app import create_app
from myflaskapp.settings import DevConfig, ProdConfig
import requests
import datetime as dt
import pytest
from myflaskapp.user.models import Role, User
from myflaskapp.item.models import Item
from .factories import UserFactory
import requests
from bs4 import BeautifulSoup
import datetime as dt


class MyTest(LiveServerTestCase):

    def create_app(self):
        app = create_app(DevConfig)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 55531
        return app
        
    def test_server_is_up_and_running(self):
        #server_url = self.get_server_url()
        #print("SERVER URL:{}".format(server_url))
        response = requests.get(self.get_server_url())
        self.assertEqual(response.status_code, 200)

    def test_home_page_can_save_a_POST_request(self): 
        test_list_data = "TERRY BATES MFR"
        client = requests.session()
        url = self.get_server_url() + '/lists/'
        print(url)
        get_result = client.get(url)
        soup = BeautifulSoup(get_result.text, 'html.parser')

        # Find the input tag
        input = soup.input

        csrf_token_value = input['value']
        print(input['value'])

        # Create dictionary to store POST params
        list_data = {'todo-item':test_list_data, 'todo-csrf_token':csrf_token_value}

        post_result = client.post(url, data=list_data, headers=dict(Referer=url))
        # Assert that our test data is in result
        assert test_list_data in post_result.text

        # Assert we have one item in DB
        #assert len(Item.query.all()) == 1
        

