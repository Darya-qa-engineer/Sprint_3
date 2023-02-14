from selenium.webdriver.common.by import By

from test_const import Locators
from test_util import User


class RegForm:
    def __init__(self, driver):
        self.driver = driver
        self.form = driver.find_element(By.XPATH, Locators.REG_FORM)

    def set_name(self, value):
        self.form.find_element(By.XPATH, Locators.REG_FORM_INPUT_NAME).send_keys(value)

    def set_email(self, value):
        self.form.find_element(By.XPATH, Locators.REG_FORM_INPUT_EMAIL).send_keys(value)

    def set_password(self, value):
        self.form.find_element(By.XPATH, Locators.REG_FORM_INPUT_PASS).send_keys(value)

    def submit(self):
        self.form.find_element(By.XPATH, Locators.REG_FORM_SUBMIT_BTN).click()

    def set_user_data(self, user: User):
        self.set_name(user.name)
        self.set_password(user.password)
        self.set_email(user.email)