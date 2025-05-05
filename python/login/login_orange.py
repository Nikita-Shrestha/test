from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
login_url = "https://opensource-demo.orangehrmlive.com/"
driver.get(login_url)

wait = WebDriverWait(driver, 10)

def login(username, password):
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))

    username_field.clear()
    password_field.clear()

    username_field.send_keys(username)
    password_field.send_keys(password)

    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

# Test with incorrect credentials
login("wronguser", "wrongpass")
error_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='alert']"))).text
assert "Invalid credentials" in error_message
print("✅ Incorrect login test passed.")

# Test with correct credentials
login("Admin", "admin123")
success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Time at Work']"))).text
assert success_message == "Time at Work"
print("✅ Correct login test passed.")

driver.quit()