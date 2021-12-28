import logging

logger = logging.getLogger(__name__)


def test_get_userlist(get_userlist):
    logger.info('test_get_userlist info')
    logger.warning('test_get_userlist warning')
    logger.error('test_get_userlist error')
    logger.critical('test_get_userlist critical')
    assert get_userlist == 'umnik vorchun veselchak sonya skromink chihun prostak', "where are the seven gnomes?"


def test_get_departament_userlist(get_departament_userlist):
    logger.info('test_get_departament_userlist info')
    logger.warning('test_get_departament_userlist warning')
    logger.error('test_get_departament_userlist error')
    logger.critical('test_get_departament_userlist critical')
    assert get_departament_userlist == 'umnik veselchak skromink prostak', "where are the four dwarves?"


def test_get_unkdepartament_userlist(get_unkdepartament_userlist):
    logger.info('test_get_unkdepartament_userlist info')
    logger.warning('test_get_unkdepartament_userlist warning')
    logger.error('test_get_unkdepartament_userlist error')
    logger.critical('test_get_unkdepartament_userlist critical')
    assert get_unkdepartament_userlist == '', "what's happening?"
