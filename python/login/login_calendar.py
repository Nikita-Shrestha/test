from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Edge WebDriver
driver = webdriver.Edge()
driver.maximize_window()

# Open Login Page
login_url = "https://calander-dash.cellapp.co/#/login"
driver.get(login_url)

# Credentials
username = "admin@cellapp.co"
password = "Cell@pp123"

# Wait for the username field and enter credentials
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']")))
password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))

username_field.send_keys(username)
password_field.send_keys(password)

# Click Login Button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']")))
login_button.click()

# Wait for the page to load after login
success_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h5[normalize-space()='Apps Download and Registration Insights']")))

# Validate successful login
assert success_element.text == "Apps Download and Registration Insights", "Login failed or text mismatch!"

# Close the browser
driver.quit()

