from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from test_const import Locators, Const


class ContentHeader:
    def __init__(self, el: WebElement, name):
        self.name = name
        self.el = el


class Tab:
    def __init__(self, el: WebElement, name, linked_header: ContentHeader):
        self.name = name
        self.el = el
        self.header = linked_header

    def select(self):
        self.el.click()

    def is_selected(self):
        return Const.CLS_BURGER_CONSTRUCTOR_ING_TAB_SELECTED in self.el.get_attribute('class')


class BurgerConstructor:
    def __init__(self, driver):
        self.driver = driver
        self.body: WebElement = driver.find_element(By.XPATH, Locators.BURGER_CONSTRUCTOR_ING_BODY)
        self.tabs = self.parse_tabs()

    def parse_tabs(self):
        tabs = {}
        els = self.body.find_elements(By.XPATH, Locators.BURGER_CONSTRUCTOR_ING_TAB)
        for el in els:
            text = el.text
            header = self.body.find_element(By.XPATH, Locators.BURGER_CONSTRUCTOR_ING_HEADER_BY_TEXT(text))
            linked_header = ContentHeader(header, header.text)
            tabs[text] = Tab(el, text, linked_header)
        return tabs

    def get_tabs_list(self):
        return list(self.tabs.values())

    def get_tab(self, name):
        return self.tabs.get(name)