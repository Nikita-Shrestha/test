import pytest
from selenium import webdriver
@pytest.fixture()
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def base_url():
    return "https://automationexercise.com/"

