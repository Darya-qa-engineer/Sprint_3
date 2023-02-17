import pytest
from selenium.webdriver.support.wait import WebDriverWait

from test_util import User, Generate
from selenium import webdriver


@pytest.fixture
def default_user():
    return User('Дарья', 'sergeeva06261@ya.ru', '8Zho04A9')


@pytest.fixture
def fake_user():
    return Generate.user()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    _wait = WebDriverWait(driver, 5)
    yield _wait
