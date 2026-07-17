import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

website_url = "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
driver.get(website_url)

driver.execute_script("window.scrollTo(0,0)")

# 1. Locate the dropdown element by its ID, Name, or XPath
dropdown_element = driver.find_element(By.ID, "state")

target_value = "NCR"

# 2. Wrap the element in Selenium's Select class
select_object = Select(dropdown_element)

# select_object.select_by_value("NCR")
# select_object.select_by_index(1)

all_options = select_object.options

time.sleep(5)

for option in all_options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
    else:
        print(f"Option '{target_value}' not found")

# 3. Retrieve all option elements within the dropdown
# all_options = select_object.options

# 4. Iterate and print the text of each option
for option in all_options:
    print(option.text)

# 5 . Check options count
option_count = len(all_options)
print(option_count)

expected_count = 5

if option_count == expected_count:
    print("Option count is matched")
else:
    print("Option count is mismatched")


time.sleep(5)
driver.close()