import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.maximize_window()
driver.execute_script("window.scrollTo(0,700)")

website_url = "https://assertqa.com/practice/webtables"

driver.get(website_url)

table_rows = "//table/tbody/tr"
next_button = "button[data-cy='pagination-next']"

total_rows = 0
page_number = 1

while True:

    # Wait until rows are visible
    rows = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, table_rows))
    )

    current_page_count = len(rows)
    total_rows += current_page_count

    print(f"Page {page_number}: {current_page_count} rows")

    targeted_email = "amanda.a@company.com"
    found = False
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            if targeted_email in cell.text:
                print(f"Found email: {targeted_email}")
                found = True
                break
        if found:
            break
    if not found:
        print("Email not found")

    # Find Next button
    next_btn = driver.find_element(By.CSS_SELECTOR, next_button)

    time.sleep(2)

    # Check if Next is disabled
    if next_btn.get_attribute("disabled") is not None:
        break

    # Store current first row text
    first_row = rows[0].text

    next_btn.click()

    # Wait for table to refresh
    wait.until(
        lambda d: d.find_elements(By.XPATH, table_rows)[0].text != first_row
    )

    page_number += 1

print(f"\nTotal rows counted: {total_rows}")

text = driver.find_element(By.CSS_SELECTOR, "div[class='mt-3 sm:mt-4 text-xs sm:text-sm text-secondary-400']").text
expected_results = int(text.split()[3])

# print(total)
if total_rows == expected_results:
    print(f"Row count validation passed!")
else:
    print(f"Row count validation failed!")


driver.quit()
