# Automation Project with Selenium & Python 🧪🕸️

This is an automated testing project for an e-commerce website, created as part of an automation course.

The project includes:

* Login tests (positive & negative)
* Tests for Homepage, Search, My Account, and Cart
* Page Object Model (with a Base Page class)
* Pytest markers for selective test runs
* Allure reporting with tags (Suite, Story, Severity)
* Automatic screenshot capture on test failures

---

## 🚀 Running the Tests

Make sure all required dependencies are installed:

```bash
pip install -r requirements.txt
```

### Run all tests:

```bash
pytest
```

### Run tests from a specific file:

```bash
pytest tests/test_login.py
```

### Run tests by marker:

```bash
pytest -m search
```

### Run with Allure report:

```bash
pytest --alluredir=reports/
allure serve reports/
```

---

## 🔐 Login Configuration – `config.json`

Some tests require login credentials (username + password).
**This file is excluded from the repository for security reasons.**

Create a new file named `config.json` with the following structure:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

You can also use the provided `config.json.example` as a template.

---

## 📁 Project Structure

```plaintext
project-root/
│
├── pages/                   # Page Object classes for each page
│   ├── base_page.py
│   ├── login.py
│   ├── home_page.py
│   ├── search.py
│   ├── my_account.py
│   └── cart_area.py
│
├── tests/                   # Test files + conftest
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_home_page.py
│   ├── test_search.py
│   ├── test_my_account.py
│   └── test_cart.py
│
├── config.json              # Private file (excluded from Git)
├── config.json.example      # Example config file
├── requirements.txt         # Project dependencies
├── pytest.ini               # Pytest markers & configuration
├── reports/                 # Allure reports (in .gitignore)
├── STD_TestCases.xlsx       # Test cases documentation
├── .gitignore
└── README.md
```

---

## 🧩 Technologies Used

* Python 3.10+
* Selenium
* Pytest
* Allure
* Page Object Model

---

## 📌 Notes

* Credentials are stored in an external `config.json` file (not included in GitHub).
* Tests were executed on Google Chrome.
* Some test cases from the STD document are covered as part of broader tests, so numbering may differ.
* `reports/` (Allure results) is ignored in Git for cleaner repository history.
* The project includes both code-based tests and a separate STD file with documented test cases.
* Detailed test cases are available in `STD_TestCases.xlsx` (download to view).


---

✅ Ready to run and extend!