import time

import requests
import selenium
from requests.exceptions import RequestException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 5)

website_url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(website_url)

alerts_section_class = "example"

# Wait until Alerts Section Appear
alerts_section_appear = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, alerts_section_class)))

# Alert One
alert_button_one = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
alert_button_one.click()

alert_one = driver.switch_to.alert
alert_text_one = alert_one.text
print("Alert text One:",alert_one.text)

time.sleep(3)

alert_one.accept()

#Alert Two
alert_button_two = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
alert_button_two.click()

alert_two = driver.switch_to.alert
alert_text_two = alert_two.text
print("Alert text Two:",alert_two.text)

time.sleep(3)

alert_two.accept()

time.sleep(3)
alert_button_two.click()
alert_two = driver.switch_to.alert
alert_two.dismiss()

time.sleep(3)
#Alert Three
alert_button_three = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
alert_button_three.click()

alert_three = driver.switch_to.alert
alert_three.send_keys("This is testing with Selenium using python.")
time.sleep(3)
alert_three.accept()

time.sleep(3)
alert_button_three.click()
alert_three = driver.switch_to.alert
alert_three.dismiss()

time.sleep(5)
driver.quit()
