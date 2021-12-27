

def test_get_userlist(get_userlist):
    assert get_userlist == 'umnik vorchun veselchak sonya skromink chihun prostak', "where are the seven gnomes?"


def test_get_departament_userlist(get_departament_userlist):
    assert get_departament_userlist == 'umnik veselchak skromink prostak', "where are the four dwarves?"


def test_get_unkdepartament_userlist(get_unkdepartament_userlist):
    assert get_unkdepartament_userlist == '', "what's happening?"
