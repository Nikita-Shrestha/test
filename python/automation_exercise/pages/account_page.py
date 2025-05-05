from .base_page import BasePage
from selenium.webdriver.common.by import By
import random
import string


class AccountPage(BasePage):
    radio_title1 = (By.XPATH, "//input[@id='id_gender1']")
    radio_title2 = (By.XPATH, "//input[@id='id_gender2']")
    password_field = (By.XPATH, "//input[@id='password']")
    first_name = (By.XPATH, "//input[@id='first_name']")
    last_name = (By.XPATH, "//input[@id='last_name']")
    dob_day = (By.XPATH, "//select[@id='days']")
    dob_month = (By.XPATH, "//select[@id='months']")
    dob_year = (By.XPATH, "//select[@id='years']")
    company_name = (By.XPATH, "//input[@id='company']")
    address1_field = (By.XPATH, "//input[@id='address1']")
    address2_field = (By.XPATH, "//input[@id='address2']")
    street_field = (By.XPATH, "//input[@id='state']")
    city_field = (By.XPATH, "//input[@id='city']")
    zipcode_field = (By.XPATH, "//input[@id='zipcode']")
    mobile_field = (By.XPATH, "//input[@id='mobile_number']")
    create_btn = (By.XPATH, "//button[normalize-space()='Create Account']")
    continue_btn = (By.XPATH, "//a[normalize-space()='Continue']")

    def fill_account(self, gender="", password="", first="", last="", day="", month="", year="", company="", add1="", add2="", street="", city="",zip="", mobile=""):
        if gender.lower() == "mr":
            self.click_element(self.radio_title1)
        else:
            self.click_element(self.radio_title2)

        self.enter_text(self.password_field, password)
        self.enter_text(self.first_name, first)
        self.enter_text(self.last_name, last)
        self.select_dropdown(self.dob_day, day)
        self.select_dropdown(self.dob_month, month)
        self.select_dropdown(self.dob_year, year)
        self.enter_text(self.company_name, company)
        self.enter_text(self.address1_field,add1)
        self.enter_text(self.address2_field,add2)
        self.enter_text(self.street_field,street)
        self.enter_text(self.city_field, city)
        self.enter_text(self.zipcode_field, zip)
        self.enter_text(self.mobile_field,mobile)
        self.click_element(self.create_btn)

    def generate_random_data(self):
        first_name = "User" + ''.join(random.choices(string.ascii_letters, k=5))
        last_name = "Test" + ''.join(random.choices(string.ascii_letters,k=5))
        password = "Pass@" + ''.join(random.choices(string.ascii_letters, k=5))
        company = "Company" + ''.join(random.choices(string.ascii_letters, k=5))
        address1 = str(random.randint(100,999)) + "Main Street"
        address2 = str(random.choices(string.ascii_letters,k=5)) + ",Nepal"
        street = random.choice(["abc","def", "ghi", "jkl", "mno"])
        city = random.choice(["onm", "lkj", "ihg", "fed", "cba"])
        zipno = random.randint(100,999)
        mobile = ''.join(random.choices(string.digits,k=10))
        gender = random.choice(["mr","mrs"])
        dob_day = str(random.randint(1,30))
        dob_month = str(random.randint(1,12))
        dob_year = str(random.randint(1970,2005))

        return {
            "first" : first_name,
            "last" : last_name,
            "password" : password,
            "gender" : gender,
            "add1" : address1,
            "add2" : address2,
            "street" : street,
            "city" : city,
            "day" : dob_day,
            "month" : dob_month,
            "year" : dob_year,
            "company" : company,
            "zip" : zipno,
            "mobile" : mobile
        }

    def fill_account_data(self):
        data = self.generate_random_data()
        self.fill_account(**data)

    def account_created(self):
        self.click_element(self.continue_btn)




