import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

website_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver.get(website_url)

driver.minimize_window()
time.sleep(2)
driver.fullscreen_window()
time.sleep(2)
driver.maximize_window()

password_reset_text = driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header")
password_reset_text.click()

time.sleep(5)
driver.back()

time.sleep(5)
driver.forward()

time.sleep(5)
driver.refresh()

time.sleep(5)
driver.close()