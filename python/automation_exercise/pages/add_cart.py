from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class AddCart(BasePage):
    add_cart = (By.XPATH, "//button[normalize-space()='Add to cart']")
    modal = (By.XPATH, "//div[@class='modal-content']")
    view_cart = (By.XPATH, "//u[normalize-space()='View Cart']")


    def product_detail(self):
        # Wait for the "Add to cart" button to be clickable
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.add_cart))
        button = self.driver.find_element(*self.add_cart)

        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_cart))

        # JavaScript click
        self.driver.execute_script("arguments[0].click();", button)

        # Wait for the modal to appear
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.modal))

        #Click view
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.view_cart)).click()