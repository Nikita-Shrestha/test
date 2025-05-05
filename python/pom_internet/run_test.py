import time

import pytest
from pages.home_page import HomePage


def test_go_to_ab_testing(setup_driver, base_url):
    driver = setup_driver
    home_page = HomePage(driver)

    home_page.open_page(base_url)
    home_page.go_to_ab()
    time.sleep(2)

def test_go_to_add_remove(setup_driver, base_url):
    driver = setup_driver
    home_page = HomePage(driver)

    home_page.open_page(base_url)
    home_page.go_to_add_remove()
    time.sleep(2)

def test_go_to_checkbox(setup_driver, base_url):
    driver = setup_driver
    home_page = HomePage(driver)

    home_page.open_page(base_url)
    home_page.go_to_checkbox()
    home_page.select_checkbox()
    home_page.deselect_checkbox()
    time.sleep(2)

def test_go_to_context_menu(setup_driver, base_url):
    driver = setup_driver
    home_page = HomePage(driver)

    home_page.open_page(base_url)
    home_page.go_to_context_menu()
    home_page.go_to_right_click()
    time.sleep(4)

@pytest.mark.parametrize("username, password, expected", [
    ("wronguser", "wrongpassword", False),
    ("tomsmith", "SuperSecretPassword!", True)
])
def test_go_to_login(setup_driver, base_url, username, password, expected):
    driver = setup_driver
    home_page = HomePage(driver)

    home_page.open_page(base_url)
    home_page.go_to_login()
    home_page.login(username, password)
    time.sleep(3)






