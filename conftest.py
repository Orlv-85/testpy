import pytest
import requests

class UsersClient:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get_users (self, departament):
         if departament==0:

           resp=requests.get('%s%s/users'%(self.host, self.port))

         else:

           resp=requests.get('%s%s/users'%(self.host, self.port), {'departament':'%s'%(departament)})

         return resp.text

uc=UsersClient('http://127.0.0.1', ':5000')

@pytest.fixture()
def get_userlist():
    resp=uc.get_users (0)
    return resp

@pytest.fixture()
def get_departament_userlist():
    resp=uc.get_users ('Dwarf')
    return resp

@pytest.fixture()
def get_unkdepartament_userlist():
    resp=uc.get_users ('Dvarf')
    return resp
