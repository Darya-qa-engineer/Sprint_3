from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from models.login_form import LoginForm
from models.reg_form import RegForm
from test_const import Locators, Const
from test_asserts import assert_logged_in_on_root


def test_registration(driver, wait, fake_user):
    driver.get(Const.ROOT_URL)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))
    wait.until(EC.presence_of_element_located((By.XPATH, Locators.REG_PAGE_ANCHOR)))

    driver.find_element(By.XPATH, Locators.REG_PAGE_ANCHOR).click()

    wait.until(EC.url_contains(Const.PATH_REG))

    form = RegForm(driver)
    form.set_user_data(fake_user)
    form.submit()

    wait.until(EC.url_matches(Const.PATH_LOGIN))
    login_form = LoginForm(driver)
    login_form.set_user_data(fake_user)
    login_form.submit()

    wait.until(EC.url_matches(Const.ROOT_URL))
    assert_logged_in_on_root(driver, wait)


def test_registration_without_name(driver, wait, fake_user):
    driver.get(Const.ROOT_URL)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))
    wait.until(EC.presence_of_element_located((By.XPATH, Locators.REG_PAGE_ANCHOR)))

    driver.find_element(By.XPATH, Locators.REG_PAGE_ANCHOR).click()

    wait.until(EC.url_contains(Const.PATH_REG))

    current_url = driver.current_url

    form = RegForm(driver)
    form.set_email(fake_user.email)
    form.set_password(fake_user.password)
    form.submit()

    assert current_url == driver.current_url
