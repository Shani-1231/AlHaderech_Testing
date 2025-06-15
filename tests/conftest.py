import json
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

@pytest.fixture
def logged_in_user(browser):
    # טוען את פרטי המשתמש
    config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
    with open(config_path) as f:
        creds = json.load(f)
    # גישה לעמוד ההתחברות
    browser.get("https://al-haderech.co.il/my-account/")
    wait = WebDriverWait(browser, 10)
    # מילוי פרטי התחברות
    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(creds["username"])
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(creds["password"])
    login_button = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
    browser.execute_script("arguments[0].click();", login_button)
    # המתנה להופעת הודעת ברכה - סימן שהמשתמש מחובר
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//p[@data-fontsize])[1]")))
    # מעבר לעמוד הבית
    browser.get("https://al-haderech.co.il/")
    return browser




