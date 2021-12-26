import pytest
import ClientFlasktest

gweb=Get_webtest()

@pytest.fixture()
gweb.get_users(0,0)

def test_response(get_users):
        assert get_users == '<Response [200]>'
