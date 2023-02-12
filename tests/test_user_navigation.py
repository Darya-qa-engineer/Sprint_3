from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from models.login_form import LoginForm
from test_const import Locators, Const
from test_util import DefaultUser


def test_user_navigation_to_personal_account():
    driver = webdriver.Chrome()
    driver.get(Const.ROOT_URL)
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))

    form = LoginForm(driver)
    form.set_email(DefaultUser.email)
    form.set_password(DefaultUser.password)
    form.submit()

    wait.until(EC.url_to_be(Const.ROOT_URL))

    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BTN).click()
    wait.until(EC.url_contains(Const.PATH_ACCOUNT))

    wait.until(EC.visibility_of_element_located((By.XPATH, Locators.ACCOUNT_PAGE_BODY)))

    driver.quit()

def test_user_navigation_to_constructor():
    driver = webdriver.Chrome()
    driver.get(Const.ROOT_URL)
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))

    form = LoginForm(driver)
    form.set_email(DefaultUser.email)
    form.set_password(DefaultUser.password)
    form.submit()

    wait.until(EC.url_to_be(Const.ROOT_URL))

    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BTN).click()
    wait.until(EC.url_contains(Const.PATH_ACCOUNT))

    wait.until(EC.visibility_of_element_located((By.XPATH, Locators.ACCOUNT_PAGE_BODY)))

    driver.find_element(By.XPATH, Locators.HEADER_CONSTRUCTOR_LINK).click()
    wait.until(EC.url_to_be(Const.ROOT_URL))

    driver.quit()


def test_user_navigation_to_constructor_via_logo():
    driver = webdriver.Chrome()
    driver.get(Const.ROOT_URL)
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))

    form = LoginForm(driver)
    form.set_email(DefaultUser.email)
    form.set_password(DefaultUser.password)
    form.submit()

    wait.until(EC.url_to_be(Const.ROOT_URL))

    driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BTN).click()
    wait.until(EC.url_contains(Const.PATH_ACCOUNT))

    wait.until(EC.visibility_of_element_located((By.XPATH, Locators.ACCOUNT_PAGE_BODY)))

    driver.find_element(By.XPATH, Locators.HEADER_LOGO).click()
    wait.until(EC.url_to_be(Const.ROOT_URL))

    driver.quit()