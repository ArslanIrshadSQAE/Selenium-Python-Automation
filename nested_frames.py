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

website_url = "https://the-internet.herokuapp.com/nested_frames"
driver.get(website_url)

iframe_xpath = "//html//frameset"

# Wait until Iframe Div Appear
iframes_appear = wait.until(EC.presence_of_all_elements_located((By.XPATH, iframe_xpath)))

#Switch to Top Framer
driver.switch_to.frame("frame-top")

#Switch to Middle Framer
driver.switch_to.frame("frame-middle")

middle_frame_content = driver.find_element(By.ID,"content").text
print("Content in the Middle frame:",middle_frame_content)

driver.switch_to.default_content()

#Switch to Bottom Frame
driver.switch_to.frame("frame-bottom")

bottom_frame_content = driver.find_element(By.TAG_NAME,"body").text
print("Content in the Bottom frame:",bottom_frame_content)


time.sleep(5)
driver.quit()
