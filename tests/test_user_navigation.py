from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from models.login_form import LoginForm
from test_const import Locators, Const, Strings


def test_user_navigation_to_personal_account(driver, wait, default_user):
    driver.get(Const.ROOT_URL)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))

    form = LoginForm(driver)
    form.set_user_data(default_user)
    form.submit()

    wait.until(EC.url_to_be(Const.ROOT_URL))

    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BTN).click()
    wait.until(EC.url_contains(Const.PATH_ACCOUNT))

    wait.until(EC.visibility_of_element_located((By.XPATH, Locators.ACCOUNT_PAGE_BODY)))

    btn = driver.find_element(By.XPATH, Locators.LOGOUT_BTN)
    assert btn.text == Strings.LOGOUT and btn.is_displayed()


def test_user_navigation_to_constructor(driver, wait, default_user):
    driver.get(Const.ROOT_URL)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))

    form = LoginForm(driver)
    form.set_user_data(default_user)
    form.submit()

    wait.until(EC.url_to_be(Const.ROOT_URL))

    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BTN).click()
    wait.until(EC.url_contains(Const.PATH_ACCOUNT))

    wait.until(EC.visibility_of_element_located((By.XPATH, Locators.ACCOUNT_PAGE_BODY)))

    driver.find_element(By.XPATH, Locators.HEADER_CONSTRUCTOR_LINK).click()
    wait.until(EC.url_to_be(Const.ROOT_URL))

    header = driver.find_element(By.XPATH, Locators.MAIN_PAGE_MAIN_HEADER)
    assert header.text == Strings.MAIN_PAGE_HEADER and header.is_displayed()


def test_user_navigation_to_constructor_via_logo(driver, wait, default_user):
    driver.get(Const.ROOT_URL)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))

    form = LoginForm(driver)
    form.set_user_data(default_user)
    form.submit()

    wait.until(EC.url_to_be(Const.ROOT_URL))

    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BTN).click()
    wait.until(EC.url_contains(Const.PATH_ACCOUNT))

    wait.until(EC.visibility_of_element_located((By.XPATH, Locators.ACCOUNT_PAGE_BODY)))

    driver.find_element(By.XPATH, Locators.HEADER_LOGO).click()
    wait.until(EC.url_to_be(Const.ROOT_URL))

    header = driver.find_element(By.XPATH, Locators.MAIN_PAGE_MAIN_HEADER)
    assert header.text == Strings.MAIN_PAGE_HEADER and header.is_displayed()

