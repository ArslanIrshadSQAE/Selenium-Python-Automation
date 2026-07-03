from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://selenium.dev")
driver.maximize_window()
title = driver.title
print(title)
assert "Selenium123" in title
# driver.quit()