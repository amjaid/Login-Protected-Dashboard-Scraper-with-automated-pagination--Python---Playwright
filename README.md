EMPLOYEE DATA SCRAPER (PLAYWRIGHT + PYTHON)

This project is a Python automation and web scraping script that logs into a web-based HR system (OrangeHRM demo)
and extracts employee information using Playwright (Sync API).

The scraper supports PAGINATION, meaning it automatically navigates through all available pages
and collects employee data from each page before exporting it to CSV and Excel formats.

NOTE:
This project uses PUBLIC demo credentials provided by OrangeHRM for learning and testing purposes.

--------------------------------------------------
FEATURES
--------------------------------------------------

- Automated login using Playwright (Sync API)
- Navigation to the PIM (Employee Information) section
- Scrapes employee details:
  - Employee ID
  - First Name
  - Last Name
  - Job Title
  - Employment Type
  - Department
- Automatically handles pagination (Next Page button)
- Scrapes data from ALL available pages
- Saves extracted data to:
  - employees.csv
  - employee_data.xlsx
- Captures a full-page screenshot after scraping
- Modular code using helper functions
- Uses reliable CSS selectors for stable scraping

--------------------------------------------------
TECHNOLOGIES USED
--------------------------------------------------

- Python 3.14
- Playwright (Sync API)
- Pandas
- OpenPyXL
- Chromium Browser

--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

employee-data-scraper/
├── scraper.py                 # Main scraping script with pagination support

├── config.py                  # Configuration file (credentials & base URL)

├── employees.csv              # Scraped employee data (CSV)

├── employee_data.xlsx         # Scraped employee data (Excel)

├── full_page_screenshot.png   # Full-page screenshot after scraping

├── requirements.txt           # Python dependencies

├── .gitignore                 # Git ignored files

└── README.txt                 # Project documentation

--------------------------------------------------
CONFIGURATION
--------------------------------------------------

DO NOT CHANGE THIS SECTION.
These credentials are PUBLIC demo credentials provided by OrangeHRM.

BASE_URL = "https://opensource-demo.orangehrmlive.com"
User_name = "Admin"
Pass_word = "admin123"

--------------------------------------------------
HOW IT WORKS
--------------------------------------------------

1. Launches a Chromium browser using Playwright
2. Logs into the OrangeHRM demo website
3. Navigates to the PIM module
4. Scrapes employee data from the current page
5. Clicks the "Next Page" button if available
6. Repeats scraping until the last page is reached
7. Stores all collected data in memory
8. Exports the data to CSV and Excel files
9. Takes a full-page screenshot for verification

--------------------------------------------------
INSTALLATION
--------------------------------------------------

Step 1: Clone the repository

git clone https://github.com/amjaid/Login-Protected-Dashboard-Scraper-with-automated-pagination--Python---Playwright.git
cd Login-Protected-Dashboard-Scraper-with-automated-pagination--Python---Playwright

Step 2: Install dependencies

pip install playwright pandas openpyxl

Step 3: Install Playwright browsers

playwright install

--------------------------------------------------
USAGE
--------------------------------------------------

Run the scraper using:

python scraper.py

--------------------------------------------------
OUTPUT
--------------------------------------------------

After execution, the following files will be generated:

- employees.csv
- employee_data.xlsx
- full_page_screenshot.png

The console will also display:
- Number of employee cards per page
- Current page number being scraped
- Total employee records scraped

--------------------------------------------------
AUTHOR
--------------------------------------------------

Abdullah Mohammad Jaid

Website: https://amjaid.com

--------------------------------------------------
LICENSE
--------------------------------------------------

This project is intended for EDUCATIONAL and PERSONAL USE only.

Please ensure you comply with the target website’s Terms of Service
before performing any scraping activities.
