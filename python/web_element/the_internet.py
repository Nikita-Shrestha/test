from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
# Function to initialize the WebDriver


def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

# Function to click an element when it's clickable
def click_element(driver, locator_type, locator_value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((locator_type, locator_value))
        )
        element.click()
    except Exception as e:
        print(f"Error clicking element {locator_value}: {e}")


def drag_drop(driver, source_locator, target_locator):
    try:
        # find the source and target element
        source_element = driver.find_element(*source_locator)
        target_element = driver.find_element(*target_locator)
        #drag and drop action
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element,target_element).perform()
    except Exception as e:
        print(f"An error occured:{e}")


#function to check or uncheck checkboxes(selects the checkbox if not selected unchecks if selected
def toggle_checkbox(driver, locator_type, locator_value):
    checkbox = driver.find_element(locator_type, locator_value)
    if not checkbox.is_selected():
        checkbox.click()
    else:
        checkbox.click()

#function to select dropdown option
def select_dropdown(driver, dropdown_id, option_text):
    dropdown_element = driver.find_element(By.ID, dropdown_id)
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text(option_text)

#function to right click
def right_click(driver, locator_type, locator_value, timeout=10):
    try:
        element1 = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )

        # Execute JavaScript to simulate a right-click
        driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('contextmenu', { bubbles: true }));", element1)
        #print("JavaScript right-click triggered.")

        time.sleep(2)

        # Handle alert
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)

        # Click outside to close any remaining context menu
        actions = ActionChains(driver)
        actions.move_by_offset(-500, -500).click().perform()
       # print("Clicked outside to close context menu.")

    except Exception as e:
        print(f"Error clicking element {locator_value}: {e}")


# Function to navigate back and wait for page title
def navigate_back(driver, expected_title, timeout=10):
    driver.back()
    WebDriverWait(driver, timeout).until(EC.title_is(expected_title))

# Function to scroll down
def scroll_down(driver, pixels = 500):
    driver.execute_script(f"window.scrollBy(0, {pixels});")

#Function to upload file
def upload_file(driver, file_input_locator, file_path):
    try:
        file_input = driver.find_element(*file_input_locator)
        file_input.send_keys(file_path)
        print("File uploaded successfully")
    except Exception as e:
        print(f"Error uploading file:{e}")

#Function for login

def login(username1, password1):
    username_field = driver.find_element(By.ID,"username")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys(username1)
    password_field.send_keys(password1)

    driver.find_element(By.XPATH,"//button[@type='submit']").click()

# Main execution
with initialize_driver() as driver:
    driver.get("https://the-internet.herokuapp.com/")
    username = "admin"
    password = "admin"
    auth_url = f"http://{username}:{password}@the-internet.herokuapp.com/basic_auth"

    wait = WebDriverWait(driver, 10)

    driver.get(auth_url)
    time.sleep(3)
    navigate_back(driver, "The Internet")
    print("Basic auth successful✅ ")
    # Click "A/B Testing"
    click_element(driver, By.LINK_TEXT, "A/B Testing")
    time.sleep(3)
    navigate_back(driver, "The Internet")
    print("A/B Testing Click✅ ")

    # Click "Add/Remove Elements"
    click_element(driver, By.LINK_TEXT, "Add/Remove Elements")

    # Click "Add Element" and then "Delete"
    click_element(driver, By.XPATH, "//button[normalize-space()='Add Element']")
    click_element(driver, By.XPATH, "//button[normalize-space()='Delete']")

    # Navigate back to the main page
    navigate_back(driver, "The Internet")
    time.sleep(2)
    print("Add/Remove Elements✅ ")

    #click "Checkbox"
    click_element(driver, By.LINK_TEXT, "Checkboxes")
    toggle_checkbox(driver, By.XPATH, "(//input[@type='checkbox'])[1]")
    toggle_checkbox(driver, By.XPATH, "(//input[@type='checkbox'])[2]")
    time.sleep(2)

    #Navigate back to the main page
    navigate_back(driver, "The Internet")
    time.sleep(2)
    print("Checkboxes✅ ")

    #click Context Menu
    click_element(driver, By.LINK_TEXT, "Context Menu")
    right_click(driver, By.XPATH, "//div[@id='hot-spot']")

    time.sleep(2)

    #Navigate back to home page
    navigate_back(driver, "The Internet")
    time.sleep(2)
    print("Right Click and Enter ✅")

    #click Disappearing Elements
    click_element(driver, By.LINK_TEXT, "Disappearing Elements")
    click_element(driver, By.XPATH, "//a[normalize-space()='About']")
    time.sleep(2)
    navigate_back(driver,"The Internet")
    click_element(driver, By.XPATH, "//a[normalize-space()='Contact Us']")
    time.sleep(2)
    navigate_back(driver, "The Internet")
    click_element(driver, By.XPATH, "//a[normalize-space()='Portfolio']")
    time.sleep(2)
    navigate_back(driver, "The Internet")
    click_element(driver, By.XPATH, "//a[normalize-space()='Home']")
    time.sleep(2)
    print("Disappearing Elements ✅")

    #click Drag and Drop
    click_element(driver, By.LINK_TEXT, "Drag and Drop")
    drag_drop(driver,( By.ID,"column-a"),(By.ID,"column-b"))
    time.sleep(2)
    navigate_back(driver,"The Internet")
    time.sleep(2)
    print("Drag and Drop ✅")

    #Click Dynamic Control
    click_element(driver, By.LINK_TEXT, "Dynamic Controls")
    toggle_checkbox(driver, By.XPATH,"//input[@type='checkbox']")
    click_element(driver, By.XPATH, "//button[normalize-space()='Remove']")
    time.sleep(2)
    click_element(driver, By.XPATH,"//button[normalize-space()='Add']")
    time.sleep(4)
    navigate_back(driver, "The Internet")
    time.sleep(2)
    print("Dynamic Control ✅")

    #Click Dynamic Loading
    click_element(driver, By.LINK_TEXT, "Dynamic Loading")
    click_element(driver, By.XPATH, "//a[normalize-space()='Example 1: Element on page that is hidden']")
    click_element(driver, By.XPATH, "//button[normalize-space()='Start']")
    time.sleep(6)
    navigate_back(driver, "The Internet")
    time.sleep(1)
    navigate_back(driver, "The Internet")
    print("Dyanamic Loading✅")

    #Click Entry Ad
    click_element(driver, By.LINK_TEXT, "Entry Ad")
    click_element(driver, By.XPATH, "//p[normalize-space()='Close']")
    time.sleep(3)
    navigate_back(driver,"The Internet")
    print("Entry Ad✅")

    #Click dropdown
    click_element(driver, By.LINK_TEXT, "Dropdown")
    select_dropdown(driver,"dropdown","Option 1")
    select_dropdown(driver, "dropdown", "Option 2")
    time.sleep(2)
    navigate_back(driver, "The Internet")
    print("Dropdown✅")

    #Click Exit Intent(last)
    #scroll section
    scroll_down(driver, 900)
    time.sleep(2)

    #Click File download
    click_element(driver, By.LINK_TEXT,"File Download")
    #scroll
    scroll_down(driver,900)
    click_element(driver, By.XPATH, "//a[normalize-space()='TextDoc.txt']")
    time.sleep(2)
    navigate_back(driver, "The Internet")
    time.sleep(2)
    print("File download✅")

    #Click File Upload
    click_element(driver, By.LINK_TEXT, "File Upload")
    time.sleep(2)

    #absolute file path to be uploaded
    file_path = r"C:\Users\hp\Downloads\24. Example Defect.png"
    #upload file
    upload_file(driver, (By.ID,"file-upload"),file_path)
    click_element(driver,By.ID,"file-submit")
    time.sleep(2)
    navigate_back(driver, "The Internet") #upload page
    navigate_back(driver, "The Internet") #home page
    time.sleep(2)

    #Click Form Authentication
    click_element(driver,By.LINK_TEXT, "Form Authentication")
    #test credentials
    login("tomsmith", "SuperSecretPassword!")
    success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='example'] h2"))).text
    assert success_message == "Secure Area"

    time.sleep(2)
    click_element(driver,By.XPATH, "//a[@class='button secondary radius']")
    navigate_back(driver, "The Internet")




