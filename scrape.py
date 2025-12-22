import pandas as pd
from playwright.sync_api import sync_playwright, Playwright, expect
import time
from config import BASE_URL, User_name, Pass_word, ITEM_SELECTOR

data = []
seen_links = set()
def add_item(id, first_name, last_name):
    if id in seen_links:
        return
    seen_links.add(id)
    data.append({"id": id,
                 "First Name": first_name,
                 "Last Name": last_name})

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
    
    
    page.wait_for_selector('class="card-item card-body-slot"')
    page.screenshot(path="full_page_screenshot.png", full_page=True)

    
    for i in range(items.count.count()):
        id = items.nth(i)
        first_name = items.locator('div[data-v-6c07a142]')
        id, first_name, last_name



    browser.close()