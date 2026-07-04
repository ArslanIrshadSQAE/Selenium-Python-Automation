import time

from selenium import webdriver

viewport = [(2560,1591),(1440,875),(1024,875),(768,875),(425,875),(375,875)]

driver = webdriver.Chrome()
driver.maximize_window()

website_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver.get(website_url)



try:
    for width, height in viewport:
        driver.set_window_size(width, height)
        time.sleep(4)

finally:
    driver.close()