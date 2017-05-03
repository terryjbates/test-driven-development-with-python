import datetime as dt
import pytest
from myflaskapp.user.models import Role, User
from myflaskapp.item.models import Item
from .factories import UserFactory
import requests
from bs4 import BeautifulSoup
import datetime as dt

import pytest

from myflaskapp.user.models import Role, User

from myflaskapp.item.models import Item

from .factories import UserFactory


@pytest.mark.usefixtures('db')
class Pages:
    url = 'http://localhost:5000'
    test_list_data = "TERRY BATES MFR"
    
    def test_home_page_can_save_a_POST_request(self): 
        client = requests.session()
        get_result = client.get(url)
        soup = BeautifulSoup(get_result.text, 'html.parser')

        # Find the input tag
        input = soup.input

        csrf_token_value = input['value']
        print(input['value'])

        # Submit data with csrf token
        list_data = {'todo-item':test_list_data, 'todo-csrf_token':csrf_token_value}

        # Assert that our test data is in result
        post_result = client.post(url, data=list_data, headers=dict(Referer=url))
        assert test_list_data in post_result.text

        # Clear data
        clear_data = {'key':'clear'}
        clear_req = client.get(url, params=clear_data)
        client.close()