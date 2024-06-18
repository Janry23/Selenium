from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# load the webpage 
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# title of the webpage
title = driver.title
assert title == "Web form"

# Text Input field
textInput = driver.find_element(by=By.ID, value="my-text-id")
textInput.send_keys("Selenium")

# Dropdown menu (select)
dropdown= driver.find_element(by=By.NAME, value= "my-select")
select = Select(dropdown)
select.select_by_visible_text("One")

# Color picker
color_picker = driver.find_element(by=By.NAME, value="my-colors")
color_picker.send_keys("#ff0000")

# Password input field
password = driver.find_element(by=By.NAME, value="my-password")
password.send_keys("Password")

# Dropdown (datalist)
input_field= driver.find_element(by=By.NAME, value= "my-datalist")
# Locate the input field by Name
input_field.send_keys("New york")

# Date picker
# Wait for the date picker element to be clickable
datepicker = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "my-date"))
)
# Click on the date picker to open it (assuming it's a text input field that opens a date picker on click)
datepicker.click()
# Example: Select a date using send_keys (if the date picker supports it)
# Clear the field first (in case it already has a value)
datepicker.clear()
time.sleep(1)  # Introducing a small wait to ensure the field is cleared before typing
# Type a date (assuming the date picker accepts manual input)
datepicker.send_keys("06/24/2025")  # Adjust the date format as per your date picker's requirements

# message field
message_field = driver.find_element(by=By.NAME, value="my-textarea")
message_field.clear()
message = "Hello, this is a test message."
message_field.send_keys(message)

# File input/upload
file_input =  driver.find_element(by=By.NAME, value="my-file")
file_path = "Your Path"
file_input.send_keys(file_path)

# Input Range
# Directly setting the value using JavaScript
range_input =  driver.find_element(by=By.NAME, value="my-range")
driver.execute_script("arguments[0].value = '9';", range_input)

# Disabled input field
disabled_input = driver.find_element(by=By.NAME, value="my-disabled")
if disabled_input.is_enabled():
    print("The input is enabled. Continuing interaction")
else:
    print("The input is disabled. Attempting to enable it...")
    # Enable the input using JavaScript
    driver.execute_script("arguments[0].removeAttribute('disabled');", disabled_input)
    # Now interact with the enabled input
    disabled_input.send_keys("example_username")
# Read only input
readonly_input = driver.find_element(by=By.NAME, value="my-readonly")
# Option 2: Remove readonly attribute using JavaScript (for testing purposes)
driver.execute_script("arguments[0].removeAttribute('readonly');", readonly_input)
# Now interact with the input (after removing readonly)
readonly_input.clear()  # Clear the current value (if needed)
readonly_input.send_keys("New Value")  # Enter a new value

# Multiple checkbox
checkbox1 = driver.find_element(by=By.ID, value="my-check-1")
checkbox2 = driver.find_element(by=By.ID, value="my-check-2")
# Example 1: Check the first checkbox
if not checkbox1.is_selected():
    checkbox1.click()

# Example 2: Check the second checkbox
if not checkbox2.is_selected():
    checkbox2.click()
#checkbox1.click()
#checkbox2.click()
#if not checkbox2.is_selected(): --if iether of the option selected
    #checkbox2.click()

# input radio
radio1 =  driver.find_element(by=By.ID, value="my-radio-1")
radio2 =  driver.find_element(by=By.ID, value="my-radio-2")
radio1.click()
radio2.click()

#submit button
submit_button= driver.find_element(by=By.XPATH, value="/html/body/main/div/form/div/div[2]/button")
submit_button.click()


time.sleep(10)
driver.quit()
