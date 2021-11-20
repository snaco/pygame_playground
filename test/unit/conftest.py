"""Setup test fixtures and default values""" 
from pytest import fixture

DEFAULT_HEIGHT = 500
DEFAULT_WIDTH = 500


def pytest_configure():
    print('I am configuring')


@fixture
def game_config():
    return {
        'width': DEFAULT_WIDTH,
        'height': DEFAULT_HEIGHT
    }