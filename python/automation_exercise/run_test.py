import random
import string
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from pages.home_page import HomePage
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.product_search import ProductSearch
from pages.add_cart import AddCart
def generate_random_user():
    name = "User" + ''.join(random.choices(string.ascii_lowercase, k=10))
    email = name + "@test.com"
    return name, email


def test_go_to_signup_btn(setup_driver,base_url):
    driver = setup_driver
    home_page = HomePage(driver)

    home_page.open_page(base_url)
    home_page.go_to_signup()

    max_attempts = 5
    for _ in range(max_attempts):
        name , email = generate_random_user()
        home_page.signup(name , email)
        time.sleep(3)

        try:
            error = driver.find_element("xpath","//p[normalize-space()='Email Address already exist!']")
            print(f"{email}already exists.Trying again")
            driver.refresh()
            home_page.go_to_signup()
            continue
        except NoSuchElementException:
            print(f"{name} is a process further for signing up")
            break

    time.sleep(3)

    account_page = AccountPage(driver)
    account_page.fill_account_data()

    account_page.account_created()


@pytest.mark.parametrize("email,password, expected",[
    ("abc@email.com","111", False),
    ("ram@email.com","test", True)
])


def test_go_to_login(setup_driver,base_url,email,password,expected):
    driver = setup_driver
    login_page = LoginPage(driver)

    login_page.open_page(base_url)
    login_page.go_to_login()
    login_page.login(email,password)
    time.sleep(3)


def test_go_to_product(setup_driver,base_url):
    driver = setup_driver
    product_search = ProductSearch(driver)
    product_search.open_page(base_url)
    product_search.go_to_product()
    time.sleep(2)
    product_search.fill_search_bar()
    product_search.search()
    time.sleep(2)
    product_search.scroll_and_click()
    time.sleep(2)
    add_cart = AddCart(driver)
    add_cart.product_detail()
    time.sleep(2)









