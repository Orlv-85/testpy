import pytest
import users_client
import set_conftest

uc = users_client.UsersClient(set_conftest.host_name, set_conftest.port_name)


@pytest.fixture()
def get_userlist():
    resp = uc.get_users()
    return resp


@pytest.fixture()
def get_departament_userlist():
    resp = uc.get_users('Dwarf')
    return resp


@pytest.fixture()
def get_unkdepartament_userlist():
    resp = uc.get_users('Dvarf')
    return resp
