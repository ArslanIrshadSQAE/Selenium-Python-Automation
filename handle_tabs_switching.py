import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

website_url = "https://www.selenium.dev"
driver.get(website_url)

driver.switch_to.new_window()

driver.get("https://playwright.dev/")

number_of_tabs = len(driver.window_handles)
print(f"Number of tabs: {number_of_tabs}")

tabs_value = driver.window_handles
print(tabs_value)

current_tab = driver.current_window_handle
print(f"Current tab: {current_tab}")

driver.find_element(By.CLASS_NAME, "getStarted_Sjon").click()
first_tab = driver.window_handles[0]

if current_tab != first_tab:
    driver.switch_to.window(first_tab)
    driver.find_element(By.XPATH,"//a[@href='/downloads']").click()

time.sleep(3)
driver.quit()