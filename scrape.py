import pandas as pd
from playwright.sync_api import sync_playwright, Playwright, expect
import time
from config import BASE_URL, User_name, Pass_word
import random

wait_time = random.randint(1, 5)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(BASE_URL)

    # Log in
    page.wait_for_selector('input[placeholder="Username"]')
    page.wait_for_selector('input[placeholder="Password"]')
    
    page.fill('input[placeholder="Username"]', User_name)
    page.fill('input[placeholder="Password"]', Pass_word)

    time.sleep(wait_time)

    page.click('button[type="submit"]')
    
    time.sleep(wait_time)

    page.screenshot(path="full_page_screenshot.png", full_page=True)

    browser.close()