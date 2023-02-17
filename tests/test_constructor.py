from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from models.burger_constructor import BurgerConstructor
from models.login_form import LoginForm
from test_const import Locators, Const


def test_constructor(driver, wait, default_user):
    driver.get(Const.ROOT_URL)

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
        assert tab.is_selected()
        selected_count = 0
        for t in tabs:
            if t.is_selected():
                selected_count += 1
        assert selected_count == 1
