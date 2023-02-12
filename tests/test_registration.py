from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from models.reg_form import RegForm
from test_const import Locators, Const
from test_util import Generate


def test_registration():
    driver = webdriver.Chrome()
    driver.get(Const.ROOT_URL)
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))
    wait.until(EC.presence_of_element_located((By.XPATH, Locators.REG_PAGE_ANCHOR)))

    driver.find_element(By.XPATH, Locators.REG_PAGE_ANCHOR).click()

    wait.until(EC.url_contains(Const.PATH_REG))

    user = Generate.user()
    form = RegForm(driver)
    form.set_name(user.name)
    form.set_email(user.email)
    form.set_password(user.password)
    form.submit()

    wait.until(EC.url_matches(Const.ROOT_URL))
    driver.quit()


def test_registration_without_name():
    driver = webdriver.Chrome()
    driver.get(Const.ROOT_URL)
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))
    wait.until(EC.presence_of_element_located((By.XPATH, Locators.REG_PAGE_ANCHOR)))

    driver.find_element(By.XPATH, Locators.REG_PAGE_ANCHOR).click()

    wait.until(EC.url_contains(Const.PATH_REG))

    current_url = driver.current_url
    user = Generate.user()
    form = RegForm(driver)
    form.set_email(user.email)
    form.set_password(user.password)
    form.submit()

    assert current_url == driver.current_url
    driver.quit()
