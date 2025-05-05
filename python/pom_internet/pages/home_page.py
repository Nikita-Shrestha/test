from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class HomePage(BasePage):
    ab_test = (By.LINK_TEXT, "A/B Testing")

    add_remove = (By.LINK_TEXT, "Add/Remove Elements")

    add_btn = (By.XPATH, "//button[normalize-space()='Add Element']")
    del_btn = (By.XPATH, "//button[normalize-space()='Delete']")

    check_box = (By.LINK_TEXT, "Checkboxes")
    check_option1 = (By.XPATH, "//input[1]")
    check_option2 = (By.XPATH,"//input[2]")

    context_menu = (By.LINK_TEXT, "Context Menu")
    right_click = (By.XPATH,"//div[@id='hot-spot']")

    login_form = (By.LINK_TEXT,"Form Authentication")
    username_field = (By.XPATH, "//input[@id='username']")
    password_field = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")

    def go_to_ab(self):
        self.click_element(self.ab_test)

    def go_to_add_remove(self):
        self.click_element(self.add_remove)
        self.click_element(self.add_btn)
        self.click_element(self.del_btn)

    def go_to_checkbox(self):
        self.click_element(self.check_box)

    def select_checkbox(self):
        if not self.driver.find_element(*self.check_option1).is_selected():
            self.click_element(self.check_option1)

        if not self.driver.find_element(*self.check_option2).is_selected():
            self.click_element(self.check_option2)

    def deselect_checkbox(self):
        if self.driver.find_element(*self.check_option1).is_selected():
            self.click_element(self.check_option1)

        if self.driver.find_element(*self.check_option2).is_selected():
            self.click_element(self.check_option2)


    def go_to_context_menu(self):
        self.click_element(self.context_menu)

    def go_to_right_click(self):
        element = self.driver.find_element(*self.right_click)
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

    def go_to_login(self):
        self.click_element(self.login_form)

    def login(self, username, password):
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.click_element(self.login_button)

    def if_error_displayed(self):
        try:
            error_element = self.driver.find_element(By.XPATH,"//div[@id='flash']")
            return error_element.is_displayed()
        except NoSuchElementException:
            return False

    def is_logged(self):
        try:
            self.driver.find_element(By.XPATH,"//i[@class='icon-2x icon-signout']")
            return True
        except NoSuchElementException:
            return False




