from playwright.sync_api import sync_playwright
import pandas as pd
import time

# -------------------------
# CONFIG
# -------------------------
BASE_URL = "https://example.com/search?q=plumber"  # starting page
ITEM_SELECTOR = ".item-card"  # container of each item
TITLE_SELECTOR = ".item-title"  # inside item
LINK_SELECTOR = "a"  # inside item
NEXT_BUTTON_SELECTOR = "a.next"  # pagination button
SCROLL_LIMIT = 50  # max items per scroll session

# -------------------------
# DATA STRUCTURES
# -------------------------
data = []
seen_links = set()

# -------------------------
# FUNCTION TO ADD ITEM
# -------------------------
def add_item(title, link):
    if link in seen_links:
        return
    seen_links.add(link)
    data.append({"Title": title, "Link": link})

# -------------------------
# SCRAPING
# -------------------------
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(BASE_URL)
    page.wait_for_selector(ITEM_SELECTOR)

    while True:
        # --- Infinite scroll (optional) ---
        previous_count = 0
        while True:
            items = page.locator(ITEM_SELECTOR)
            current_count = items.count()
            if current_count == previous_count or current_count >= SCROLL_LIMIT:
                break
            previous_count = current_count
            page.mouse.wheel(0, 3000)
            page.wait_for_timeout(1000)

        # --- Extract items ---
        items = page.locator(ITEM_SELECTOR)
        for i in range(items.count()):
            item = items.nth(i)
            title = item.locator(TITLE_SELECTOR).inner_text()
            link = item.locator(LINK_SELECTOR).get_attribute("href")
            add_item(title, link)

        # --- Pagination ---
        next_button = page.locator(NEXT_BUTTON_SELECTOR)
        if next_button.count() == 0 or next_button.is_disabled():
            break
        next_button.click()
        page.wait_for_selector(ITEM_SELECTOR)
        time.sleep(1)  # small wait for content

    browser.close()

# -------------------------
# SAVE TO EXCEL
# -------------------------
df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False)

print(f"Scraping complete! Total items: {len(data)}")
