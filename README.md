# 🕵️ Employee Data Scraper (Playwright + Python)

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Sync_API-green?style=for-the-badge&logo=playwright&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-orange?style=for-the-badge)

> **A robust automation tool that logs into the login-protected OrangeHRM system, handles pagination automatically, and extracts employee data into CSV and Excel formats.**

---

## 📖 Overview

This project is a **Python-based web scraper** designed to automate data extraction from the **OrangeHRM Demo** site. It uses **Playwright (Sync API)** to handle authentication, navigate through the PIM (Employee Information) module, and traverse multiple pages of data.

**⚠️ Note:** This project uses public demo credentials provided by OrangeHRM and is intended strictly for **learning and testing purposes**.

---

## ✨ Features

### 🤖 Automation & Navigation
* **Automated Login:** Securely logs in using the Sync API.
* **Smart Pagination:** Automatically detects and clicks "Next Page" until all data is scraped.
* **Robust Selectors:** Built with stable selectors to minimize breakage.

### 📊 Data Extraction
Scrapes the following fields for every employee:
* Employee ID
* First & Last Name
* Job Title & Employment Type
* Department

### 💾 Export & Logging
* **Dual Export:** Saves data to `employees.csv` and `employee_data.xlsx`.
* **Visual Proof:** Captures a full-page screenshot after scraping (`full_page_screenshot.png`).
* **Live Feedback:** Console logs show page numbers, record counts, and total progress.

---

## 🛠️ Technologies Used

* **Python 3.14**
* **Playwright (Sync API)** - For browser automation.
* **Pandas** - For data structuring and CSV export.
* **OpenPyXL** - For Excel export.
* **Chromium** - The browser engine used for scraping.

---

## 📁 Project Structure

```text
employee-data-scraper/
├── scraper.py                 # 🚀 Main scraping script with pagination logic

├── config.py                  # ⚙️ Configuration (Base URL & Credentials)

├── requirements.txt           # 📦 Python dependencies

├── .gitignore                 # 🙈 Git ignored files

├── README.md                  # 📄 Project documentation

├── employees.csv          # 📄 Scraped data (CSV)

├── employee_data.xlsx     # 📊 Scraped data (Excel)

└── full_page_screenshot.png # 📸 Verification screenshot

⚙️ Configuration
⚠️ DO NOT MODIFY THIS SECTION IN config.py These are the official public demo credentials for OrangeHRM.

BASE_URL = "[https://opensource-demo.orangehrmlive.com](https://opensource-demo.orangehrmlive.com)"
User_name = "Admin"
Pass_word = "admin123"

🚀 Installation & Usage
Step 1: Clone the Repository
git clone [https://github.com/amjaid/Login-Protected-Dashboard-Scraper-with-automated-pagination--Python---Playwright.git](https://github.com/amjaid/Login-Protected-Dashboard-Scraper-with-automated-pagination--Python---Playwright.git)
cd Login-Protected-Dashboard-Scraper-with-automated-pagination--Python---Playwright

Step 2: Install Dependencies
pip install playwright pandas openpyxl

Step 3: Install Playwright Browsers
playwright install

Step 4: Run the Scraper
python scraper.py


🔄 How It Works
Launch: Opens a Chromium browser instance.

Auth: Logs into the OrangeHRM dashboard using demo credentials.

Navigate: Moves to the PIM (Employee List) section.

Scrape: Extracts data from the current page table.

Paginate: Checks for a "Next" button; if active, clicks and repeats Step 4.

Save: Once the last page is reached, data is compiled and saved to disk.

👤 Author
Abdullah Mohammad Jaid

🌐 Website: amjaid.com

🐙 GitHub: github.com/amjaid

📄 License & Disclaimer
This project is for educational and personal use only.

Please ensure you comply with the target website’s Terms of Service and Robots.txt policies before performing any scraping or automation activities.
