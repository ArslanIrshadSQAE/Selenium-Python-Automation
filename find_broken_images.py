import time

import requests
from requests.exceptions import RequestException
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

website_url = "https://the-internet.herokuapp.com"
driver.get(website_url)

time.sleep(3)

# 1. Collect all hrefs first

all_links = driver.find_elements(By.TAG_NAME, "a")

links = []

for link in all_links:
    href = link.get_attribute("href")

    if not href:
        continue

    if href.startswith(("javascript:", "mailto:", "tel:")):
        continue

    links.append(href)

print(f"Total valid links: {len(links)}")

headers = {
    "User-Agent": "Mozilla/5.0"
}

broken_images = []

# 2. Visit every link
for i, href in enumerate(links, start=1):

    # Skipped external links because I want to test this website
    if not href.startswith("https://the-internet.herokuapp.com"):
        print(f"{i}. Skipped external link: {href}")
        continue

    try:
        response = requests.get(href, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"{i}. Broken: {href} ({response.status_code})")
            continue

        driver.get(href)

        images = driver.find_elements(By.TAG_NAME, "img")

        print(f"{i}. {href}")
        print(f"Images found: {len(images)}")

        for img in images:
            src = img.get_attribute("src")
            if src:
                response = requests.get(src)
                if response.status_code != 200:
                    broken_images.append(src)
                    print("Broken images found")

        if broken_images:
            print(f"List of broken images:")
            for broken_image in broken_images:
                print(broken_image)
        else:
            print(f"No broken images:")

        broken_images.clear()
    except RequestException as e:
        print(f"{i}. ERROR: {href}")
        print(e)

driver.close()
