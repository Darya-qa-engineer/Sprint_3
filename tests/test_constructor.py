from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from models.burger_constructor import BurgerConstructor
from models.login_form import LoginForm
from test_const import Locators, Const


def test_user_navigation_to_constructor(default_user):
    driver = webdriver.Chrome()
    driver.get(Const.ROOT_URL)
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.XPATH, Locators.BASKET_LOGIN_BTN).click()

    wait.until(EC.url_contains(Const.PATH_LOGIN))

    form = LoginForm(driver)
    form.set_user_data(default_user)
    form.submit()

    wait.until(EC.url_to_be(Const.ROOT_URL))

    constructor = BurgerConstructor(driver)
    tabs = constructor.get_tabs_list()
    first_tab = tabs[0]

    wait.until(EC.visibility_of(first_tab.header.el))
    assert len(tabs) == 3

    tabs.reverse()
    for tab in tabs:
        tab.select()
        selected_count = 0
        for t in tabs:
            if t.is_selected():
                selected_count += 1
        assert tab.is_selected()
        wait.until(EC.visibility_of(tab.header.el))
        assert selected_count == 1
