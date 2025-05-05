from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    login_menu = (By.XPATH, "//span[@class='login pl-2']")
    username_field = (By.XPATH, "//input[@id='username']")
    password_field = (By.XPATH, "//input[@id='password']")
    login_btn = (By.XPATH, "//button[@id='loginbtn']")

    def go_to_login(self):
        self.click_element(self.login_menu)

    def login(self, username, password):
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.click_element(self.login_btn)

    def if_logged_in(self):
        try:
            return self.driver.find_element(By.XPATH,"(//img[@class='logo mr-1'])[1]").is_displayed()
        except:
            return False

    def login_failed(self):
        try:
            error = self.driver.find_element(By.ID,"yui_3_18_1_1_1746421372920_12")
            return error.is_displayed()
        except:
            return False
