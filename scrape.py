import pandas as pd
from playwright.sync_api import sync_playwright, Playwright, expect
import time
from config import BASE_URL, User_name, Pass_word, ITEM_SELECTOR

data = []
#seen_links = set()
def add_item(id, first_name, last_name, job_title, employment_type, department):
    #if id in seen_links:
    #   return
    #seen_links.add(id)
    data.append({
        "ID": id,
        "First Name": first_name,
        "Last Name": last_name,
        "Job Title": job_title,
        "Employment Type": employment_type,
        "Department": department
    })

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(BASE_URL)

    # Log in
    page.wait_for_selector('input[placeholder="Username"]')
    page.wait_for_selector('input[placeholder="Password"]')
    
    page.fill('input[placeholder="Username"]', User_name)
    page.fill('input[placeholder="Password"]', Pass_word)

    page.click('button[type="submit"]')

    # Go to employee page

    page.click('text="PIM"')

    #Start Scraping
    
    
    page.wait_for_selector('div.oxd-table-card')

    employee_cards = page.locator('div.oxd-table-card')

    card_count = employee_cards.count()
    print(f"Found {card_count} employee cards.")

    for i in range(card_count):
        card = employee_cards.nth(i)
        
        # Scrape Employee ID (2nd column)
        id_element = card.locator('div.oxd-table-row > div:nth-child(2) div')
        id = id_element.inner_text() if id_element.count() > 0 else "N/A"

        # Scrape First Name (3rd column)
        first_name_element = card.locator('div.oxd-table-row > div:nth-child(3) div')
        first_name = first_name_element.inner_text() if first_name_element.count() > 0 else "N/A"

        # Scrape Last Name (4th column)
        last_name_element = card.locator('div.oxd-table-row > div:nth-child(4) div')
        last_name = last_name_element.inner_text() if last_name_element.count() > 0 else "N/A"

        # Scrape Job Title (5th column)
        job_title_element = card.locator('div.oxd-table-row > div:nth-child(5) div')
        job_title = job_title_element.inner_text() if job_title_element.count() > 0 else "N/A"

        # Scrape Employment Type (6th column)
        employment_type_element = card.locator('div.oxd-table-row > div:nth-child(6) div')
        employment_type = employment_type_element.inner_text() if employment_type_element.count() > 0 else "N/A"

        # Scrape Department (7th column)
        department_element = card.locator('div.oxd-table-row > div:nth-child(7) div')
        department = department_element.inner_text() if department_element.count() > 0 else "N/A"

        # Add the scraped data to the list
        add_item(id, first_name, last_name, job_title, employment_type, department)

    print(f"Scraped Data: {data}")  

    df = pd.DataFrame(data)
    df.to_csv('employees.csv ', index=False)
    df.to_excel("employee_data.xlsx", index=False, engine='openpyxl')
    print("Data saved to employees.xlsx")

    page.screenshot(path="full_page_screenshot.png", full_page=True)

    browser.close()