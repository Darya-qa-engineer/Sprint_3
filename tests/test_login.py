from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from models.login_form import LoginForm
from test_util import Generate
from test_asserts import assert_logged_in_on_root
from test_const import Locators, Const, Strings


def test_login_account_via_forgot_path_back_link(driver, wait, default_user):
    driver.get(Const.ROOT_URL)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()
    wait.until(EC.url_contains(Const.PATH_LOGIN))

    driver.find_element(By.XPATH, Locators.LOGIN_PAGE_FORGOT_PASS).click()
    wait.until(EC.url_contains(Const.PATH_FORGOT_PASS))

    driver.find_element(By.XPATH, Locators.FORGOT_PASS_PAGE_LOGIN).click()
    wait.until(EC.url_contains(Const.PATH_LOGIN))

    form = LoginForm(driver)
    form.set_user_data(default_user)
    form.submit()

    wait.until(EC.url_to_be(Const.ROOT_URL))
    btn = driver.find_element(By.XPATH, Locators.BASKET_MAKE_ORDER_BTN)
    assert btn.text == Strings.MAKE_ORDER


def test_login_via_reg_page(driver, wait, default_user):
    driver.get(Const.ROOT_URL)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))
    wait.until(EC.presence_of_element_located((By.XPATH, Locators.REG_PAGE_ANCHOR)))

    driver.find_element(By.XPATH, Locators.REG_PAGE_ANCHOR).click()

    wait.until(EC.url_contains(Const.PATH_REG))

    wait.until(EC.element_to_be_clickable((By.XPATH, Locators.REG_PAGE_ALREADY_SIGNED_UP)))

    driver.find_element(By.XPATH, Locators.REG_PAGE_ALREADY_SIGNED_UP).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))

    form = LoginForm(driver)
    form.set_user_data(default_user)
    form.submit()

    wait.until(EC.url_to_be(Const.ROOT_URL))

    assert_logged_in_on_root(driver, wait)


def test_login_account_via_login_btn(driver, wait, default_user):
    driver.get(Const.ROOT_URL)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))

    form = LoginForm(driver)
    form.set_user_data(default_user)
    form.submit()

    wait.until(EC.url_to_be(Const.ROOT_URL))

    assert_logged_in_on_root(driver, wait)


def test_login_account_via_the_button_personal_account(driver, wait, default_user):
    driver.get(Const.ROOT_URL)

    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))

    form = LoginForm(driver)
    form.set_user_data(default_user)
    form.submit()

    wait.until(EC.url_to_be(Const.ROOT_URL))

    assert_logged_in_on_root(driver, wait)


def test_login_invalid_password(driver, wait, default_user):
    driver.get(Const.ROOT_URL)

    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))

    current_url = driver.current_url
    form = LoginForm(driver)
    form.set_email(default_user.email)
    form.set_password(Generate.user_password())
    form.submit()

    assert current_url == driver.current_url
