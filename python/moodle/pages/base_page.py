class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)
