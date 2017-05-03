from flask import Flask
from flask_testing import LiveServerTestCase
from myflaskapp.app import create_app
from myflaskapp.settings import DevConfig, ProdConfig
import requests


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



