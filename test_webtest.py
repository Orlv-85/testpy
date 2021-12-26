import pytest
import requests

class Get_webtest:

     def get_users (self,a,b):
         resp=requests.get('http://127.0.0.1:5000/users', {a:b})
         return resp
gu=Get_webtest()

@pytest.fixture()
def get_users1():
    resp=gu.get_users ('username','ch')
    return resp

@pytest.fixture()
def get_users2():
    resp=gu.get_users ('departament','Dvarf')
    return resp

def test_response1(get_users1):
    assert str(get_users1) == '<Response [200]>'

def test_response2(get_users1):
    assert str(get_users1.text) == 'vorchun veselchak chihun'

def test_response3(get_users2):
    assert str(get_users2.text) == 'umnik veselchak skromink prostak'
