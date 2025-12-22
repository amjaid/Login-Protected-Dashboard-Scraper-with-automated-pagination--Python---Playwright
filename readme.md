# Employee Data Scraper (Playwright + Python)

This project is a Python automation and web scraping script that logs into a web-based HR system and extracts employee information using Playwright (Sync API). The collected data is stored in both CSV and Excel formats for easy analysis and reporting.

---

## 📌 Features

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
  - `employees.csv`
  - `employee_data.xlsx`
- Captures a full-page screenshot after scraping
- Uses robust CSS selectors for data extraction

---

## 🛠️ Technologies Used

- Python 3.x
- Playwright (Sync API)
- Pandas
- OpenPyXL
- Chromium Browser

---

## 📂 Project Structure

├── scraper.py # Main scraping script
├── config.py # Configuration file (credentials & base URL)
├── employees.csv # Scraped data (CSV)
├── employee_data.xlsx # Scraped data (Excel)
├── full_page_screenshot.png # Screenshot of the employee page
└── README.md # Project documentation

## ⚙️ Configuration

BASE_URL = "https://opensource-demo.orangehrmlive.com"  # starting page
User_name = "Admin"
Pass_word = "admin123"

🚀 Installation

step -1 
git clone https://github.com/your-username/employee-data-scraper.git
cd employee-data-scraper

step -2
Install dependencies:
pip install playwright pandas openpyxl

step -3
Install Playwright browsers:
playwright install

▶️ Usage
Run the scraper using:
python scraper.py

After execution, the scraped employee data will be saved as:
employees.csv
employee_data.xlsx
A full-page screenshot will also be generated.

🧑‍💻 Author
Abdullah Mohammad Jaid
🌐 Website: https://amjaid.com

📄 License
This project is for educational and personal use.
Make sure to comply with the target website’s Terms of Service before scraping.
