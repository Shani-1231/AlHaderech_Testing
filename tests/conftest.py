import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def homepage(browser):
    browser.get("https://al-haderech.co.il/")
    return browser
# בטסט:
# def test_homepage_title(homepage):
#     assert "הדרך" in homepage.title

@pytest.fixture
def logged_in_user(browser):
    browser.get("https://al-haderech.co.il/login")
    # שלבי התחברות - לפי מה שיש באתר בפועל
    # browser.find_element(...).send_keys(...)
    # browser.find_element(...).click()
    return browser

# import json
# import os
#
# @pytest.fixture
# def logged_in_user(browser):
#     config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
#     with open(config_path) as f:
#         creds = json.load(f)
#
#     browser.get("https://al-haderech.co.il/login")
#     browser.find_element(...).send_keys(creds["username"])
#     browser.find_element(...).send_keys(creds["password"])
#     browser.find_element(...).click()
#     return browser


