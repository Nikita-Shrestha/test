from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    log_in = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    email_field = (By.XPATH, "//input[@data-qa='login-email']")
    password_field = (By.XPATH, "//input[@placeholder='Password']")
    login_btn = (By.XPATH, "//button[normalize-space()='Login']")


    def go_to_login(self):
        self.click_element(self.log_in)

    def login(self,email,password):
        self.enter_text(self.email_field, email)
        self.enter_text(self.password_field, password)
        self.click_element(self.login_btn)



