import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_page(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def select_dropdown(self, locator, value):
        dropdown = Select(self.driver.find_element(*locator))
        dropdown.select_by_value(value)