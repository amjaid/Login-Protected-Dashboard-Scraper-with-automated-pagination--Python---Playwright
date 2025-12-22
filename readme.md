EMPLOYEE DATA SCRAPER (PLAYWRIGHT + PYTHON)

This project is a Python automation and web scraping script that logs into a web-based HR system and extracts employee information using Playwright (Sync API). The collected data is stored in both CSV and Excel formats for easy analysis and reporting.

NOTE:
This project uses public demo credentials provided by OrangeHRM for learning and testing purposes.

--------------------------------------------------
FEATURES
--------------------------------------------------

- Automated login using Playwright
- Navigation to the PIM (Employee Information) section
- Scrapes employee details:
  - Employee ID
  - First Name
  - Last Name
  - Job Title
  - Employment Type
  - Department
- Saves output data to:
  - employees.csv
  - employee_data.xlsx
- Captures a full-page screenshot after scraping
- Uses structured and reliable CSS selectors

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
├── scraper.py                 # Main scraping script

├── config.py                  # Configuration file (credentials & base URL)

├── employees.csv              # Scraped employee data (CSV)

├── employee_data.xlsx         # Scraped employee data (Excel)

├── full_page_screenshot.png   # Full-page screenshot after scraping

├── requirements.txt           # Python dependencies

├── .gitignore                 # Git ignored files

├── venv/                      # Virtual environment (optional)

└── README.txt                 # Project documentation


--------------------------------------------------
CONFIGURATION
--------------------------------------------------

DO NOT CHANGE THIS SECTION.
These credentials are public demo credentials.

BASE_URL = "https://opensource-demo.orangehrmlive.com"

User_name = "Admin"

Pass_word = "admin123"

--------------------------------------------------
INSTALLATION
--------------------------------------------------

Step 1: Clone the repository

git clone https://github.com/your-username/employee-data-scraper.git
cd employee-data-scraper

Step 2: Install dependencies

pip install playwright pandas openpyxl

Step 3: Install Playwright browsers

playwright install

--------------------------------------------------
USAGE
--------------------------------------------------

Run the scraper using:

python scraper.py

After execution, the following files will be generated:

- employees.csv
- employee_data.xlsx
- full_page_screenshot.png

--------------------------------------------------
AUTHOR
--------------------------------------------------

Abdullah Mohammad Jaid

Website: https://amjaid.com

--------------------------------------------------
LICENSE
--------------------------------------------------

This project is intended for educational and personal use only.

Please ensure you comply with the target website’s Terms of Service before performing any scraping activities.
