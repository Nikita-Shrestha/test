from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)


# Function to perform login test
def login(username, password):
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    username_field.clear()
    password_field.clear()

    username_field.send_keys(username)
    password_field.send_keys(password)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()


# Test with incorrect credentials
login("wronguser", "wrongpass")
error_message = wait.until(EC.presence_of_element_located((By.ID, "flash"))).text
assert "Your username is invalid!" in error_message
print("✅ Incorrect login test passed.")

# Test with correct credentials
login("tomsmith", "SuperSecretPassword!")
success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='example'] h2"))).text
assert success_message == "Secure Area"
print("✅ Correct login test passed.")

# Close browser
driver.quit()
