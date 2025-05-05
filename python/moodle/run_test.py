import time
import pytest
from pages.login import LoginPage

@pytest.mark.parametrize("username, password, expected", [
    ("abc123", "111", False),
    ("admin_moodle", "@%$2&Av&Cm", True)
])
def test_go_to_login(setup_driver, base_url, username, password, expected):
    driver = setup_driver
    login_page = LoginPage(driver)
    login_page.open_page(base_url)
    login_page.go_to_login()
    login_page.login(username, password)
    time.sleep(3)
    if expected:
        assert login_page.if_logged_in() is True
    else:
        assert login_page.login_failed() is False