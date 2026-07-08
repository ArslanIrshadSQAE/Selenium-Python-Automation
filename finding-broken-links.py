import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

website_url = "https://jqueryui.com/"
driver.get(website_url)

# 1. Locate the link by its Tag
all_links = driver.find_elements(By.TAG_NAME,'a')

link_count = len(all_links)

print(f"Total '{link_count}' links are found")

# 2. Iterate and check valid links
valid_links = []

for link in all_links:
    href = link.get_attribute("href")

    if not href:
        continue

    if href.startswith(("javascript:", "mailto:", "tel:", "#")):
        continue

    valid_links.append(link)

print(f"Total valid links: {len(valid_links)}")


# 3. Iterate and print the broken links with status code
for count, link in enumerate(valid_links[0:], start=1):
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code == 200:
        print(f"Count: '{count}'")
    else:
        print(f"Count: '{count}' Link '{href}' is broken. Status code: '{response.status_code}'")

driver.close()