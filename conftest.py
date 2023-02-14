import pytest

from test_util import User, Generate


@pytest.fixture
def default_user():
    return User('Дарья', 'sergeeva06261@ya.ru', '8Zho04A9')


@pytest.fixture
def fake_user():
    return Generate.user()
