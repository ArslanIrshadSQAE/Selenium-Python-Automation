import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()



website_url = "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
driver.get(website_url)

driver.execute_script("window.scrollTo(0,0)")

radioboxes = driver.find_elements(By.XPATH, "//input[@type='radio']")
for radiobox in radioboxes:
    radiobox.send_keys(Keys.SPACE)

checked_count = 0

for checkbox in radioboxes:
    if radiobox.is_selected():
        checked_count += 1

expected_checked_count = 3

if checked_count == expected_checked_count:
    print("Radiobox count is matched")
else:
    print("Radiobox count is mismatched")


checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

checked_count = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1

expected_checked_count = 3

if checked_count == expected_checked_count:
    print("Checkbox count is matched")
else:
    print("Checkbox count is mismatched")
time.sleep(5)
driver.close()