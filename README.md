EMPLOYEE DATA SCRAPER
(Playwright + Python)

This project is a Python-based automation and web scraping tool that logs into a login-protected HR system (OrangeHRM Demo) and extracts employee information using Playwright (Sync API).

The scraper fully supports automatic pagination, ensuring that employee data is collected from all available pages and exported into CSV and Excel formats.

⚠️ Note
This project uses public demo credentials provided by OrangeHRM and is intended strictly for learning and testing purposes.

✨ FEATURES

Automated login using Playwright (Sync API)

Navigation to the PIM (Employee Information) module

Scrapes employee details:

Employee ID

First Name

Last Name

Job Title

Employment Type

Department

Automatic pagination handling (Next Page navigation)

Scrapes data from all available pages

Exports data to:

employees.csv

employee_data.xlsx

Captures a full-page screenshot after scraping

Modular and readable code structure

Robust selectors for stable scraping

Console logs for:

Page number

Records per page

Total records scraped

🛠️ TECHNOLOGIES USED

Python 3.14

Playwright (Sync API)

Pandas

OpenPyXL

Chromium Browser

📁 PROJECT STRUCTURE
employee-data-scraper/
├── scraper.py                 # Main scraping script with pagination

├── config.py                  # Configuration (base URL & credentials)

├── employees.csv              # Scraped employee data (CSV)

├── employee_data.xlsx         # Scraped employee data (Excel)

├── full_page_screenshot.png   # Full-page screenshot after scraping

├── requirements.txt           # Python dependencies

├── .gitignore                 # Git ignored files

└── README.md                  # Project documentation

⚙️ CONFIGURATION

⚠️ DO NOT MODIFY THIS SECTION

These are public demo credentials officially provided by OrangeHRM.

BASE_URL = "https://opensource-demo.orangehrmlive.com"
User_name = "Admin"
Pass_word = "admin123"

🔄 HOW IT WORKS

Launches a Chromium browser using Playwright

Logs into the OrangeHRM demo website

Navigates to the PIM module

Scrapes employee data from the current page

Detects and clicks the Next Page button (if available)

Repeats scraping until the last page is reached

Stores all employee data in memory

Exports data to CSV and Excel formats

Captures a full-page screenshot for verification

📦 INSTALLATION

Step 1: Clone the repository
git clone https://github.com/amjaid/Login-Protected-Dashboard-Scraper-with-automated-pagination--Python---Playwright.git
cd Login-Protected-Dashboard-Scraper-with-automated-pagination--Python---Playwright

Step 2: Install dependencies
pip install playwright pandas openpyxl

Step 3: Install Playwright browsers
playwright install

▶️ USAGE

Run the scraper with:

python scraper.py

📤 OUTPUT

After execution, the following files will be generated:

employees.csv

employee_data.xlsx

full_page_screenshot.png

The console output will display:

Number of employee cards per page

Current page being scraped

Total employee records collected

👤 AUTHOR

Abdullah Mohammad Jaid

🌐 Website: https://amjaid.com

📄 LICENSE & DISCLAIMER

This project is intended for educational and personal use only.

Please ensure that you comply with the target website’s Terms of Service
before performing any scraping or automation activities.