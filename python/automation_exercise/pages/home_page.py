from .base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    sign_up = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    name_field = (By.XPATH, "//input[@placeholder='Name']")
    email_field = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_btn = (By.XPATH, "//button[normalize-space()='Signup']")

    # Click on signup/Login
    def go_to_signup(self):

        self.click_element(self.sign_up)

    # Fill signup form and submit
    def signup(self, name, email):
        self.enter_text(self.name_field, name)
        self.enter_text(self.email_field, email)
        self.click_element(self.signup_btn)
