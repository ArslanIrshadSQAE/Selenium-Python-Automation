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
wait = WebDriverWait(driver, 10)

website_url = "https://the-internet.herokuapp.com/iframe"
driver.get(website_url)

iframe_id = "content"

# Wait until Iframe Div Appear
iframe_appear = wait.until(EC.presence_of_all_elements_located((By.ID, iframe_id)))

# close_button = driver.find_element(By.XPATH, "//button[@class='tox-notification__dismiss tox-button tox-button--naked tox-button--icon']")
# close_button.click()

iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)


Text_editor = driver.find_element(By.ID,"tinymce")
Text_editor.clear()
Text_editor.send_keys("This is testing through Selenium using Python")

time.sleep(5)

driver.switch_to.default_content()
selenium_link = driver.find_element(By.XPATH, "//a[normalize-space()='Elemental Selenium']")
selenium_link.click()


time.sleep(5)
driver.quit()
