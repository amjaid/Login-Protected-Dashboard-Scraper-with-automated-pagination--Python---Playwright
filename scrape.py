import pandas as pd
from playwright.sync_api import sync_playwright, Playwright, expect
import time
from config import BASE_URL, User_name, Pass_word

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

def scrape_current_page(page):
    #Scrape data from the current page
    page.wait_for_selector('div.oxd-table-card')
    employee_cards = page.locator('div.oxd-table-card')
    card_count = employee_cards.count()
    print(f"Found {card_count} employee cards on this page.")

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

    # Start Scraping with pagination
    page_num = 1
    
    while True:
        print(f"\nScraping page {page_num}...")
        
        # Wait for page to load and scrape data
        scrape_current_page(page)
        
        # Check if there's a next page button and if it's clickable
        next_button = page.locator('button i.bi-chevron-right')
        
        if next_button.count() > 0:
            # Check if next button is disabled (for last page)
            next_button_parent = page.locator('button i.bi-chevron-right').locator('..')
            
            # Check for disabled attribute or class that indicates the button is disabled
            is_disabled = (
                next_button_parent.get_attribute('disabled') is not None or
                'disabled' in (next_button_parent.get_attribute('class') or '') or
                '--disabled' in (next_button_parent.get_attribute('class') or '')
            )
            
            if not is_disabled:
                print("Moving to next page...")
                next_button.click()
                page_num += 1
                # Wait for page to load after clicking next
                page.wait_for_load_state('networkidle')
                time.sleep(1)  # Small delay to ensure page is fully loaded
            else:
                print("Reached the last page.")
                break
        else:
            print("No next page button found. Stopping.")
            break

    print(f"\nTotal scraped {len(data)} employee records.")
    
    df = pd.DataFrame(data)
    df.to_csv('employees.csv', index=False)
    df.to_excel("employee_data.xlsx", index=False, engine='openpyxl')
    print("Data saved to employees.xlsx and employees.csv")

    page.screenshot(path="full_page_screenshot.png", full_page=True)

    browser.close()