from .base_page import BasePage
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductSearch(BasePage):
    search_field = (By.XPATH, "//input[@id='search_product']")
    search_btn = (By.XPATH, "//button[@id='submit_search']")
    product = (By.XPATH, "//a[@href='/products']")
    search_results = (By.XPATH, "//body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='features_items']/div[2]/div[1]")
    view_btn = (By.XPATH, "//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]")


    def go_to_product(self):
        self.click_element(self.product)

    def fill_search(self, search=""):
        self.enter_text(self.search_field,search)

    def generate_random_search(self):
        search = random.choice(["polo","dress","top","pink"])

        return {
            "search": search
        }

    def fill_search_bar(self):
        data = self.generate_random_search()
        self.fill_search(**data)

    def search(self):
        self.click_element(self.search_btn)

    def scroll_and_click(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.search_results))
        results = self.driver.find_elements(*self.search_results)
        if results:
            random_result = random.choice(results)
            self.driver.execute_script("window.scrollBy(0,500);")
            time.sleep(1)
            random_result.click()

        else:
            print("No results")

        self.click_element(self.view_btn)







