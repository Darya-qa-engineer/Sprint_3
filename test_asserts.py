from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from test_const import Locators, Strings


def assert_logged_in_on_root(driver, wait):
    wait.until(EC.element_to_be_clickable((By.XPATH, Locators.BASKET_MAKE_ORDER_BTN)))
    btn = driver.find_element(By.XPATH, Locators.BASKET_MAKE_ORDER_BTN)
    assert btn.text == Strings.MAKE_ORDER and btn.is_displayed()
