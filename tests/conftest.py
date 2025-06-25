import json
import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
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
def logged_out_user(browser):
    browser.delete_all_cookies()
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
    try:
        # ננסה למצוא את הודעת הברכה ולבדוק אם היא מכילה את המילה "שלום"
        greeting_elem = wait.until(EC.visibility_of_element_located((By.XPATH, "(//p[@data-fontsize])[1]")))
        greeting_text = greeting_elem.text.strip()
        if "שלום" in greeting_text:
            print("כבר מחובר")
        else:
            raise Exception("לא נמצא טקסט של ברכת התחברות – מנסה להתחבר")
    except:
        print("לא מחובר – מנסה להתחבר")
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(creds["username"])
            wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(creds["password"])
            login_button = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
            browser.execute_script("arguments[0].click();", login_button)
            # נוודא שהתחברות הצליחה לפי הודעת "שלום"
            greeting_elem = wait.until(EC.visibility_of_element_located((By.XPATH, "(//p[@data-fontsize])[1]")))
            greeting_text = greeting_elem.text.strip()
            assert "שלום" in greeting_text, "ההתחברות נכשלה – לא הופיעה הודעת שלום"
            print("התחברות הצליחה")
        except Exception as e:
            print("שגיאה בהתחברות:", e)
            raise
    browser.get("https://al-haderech.co.il/")
    return browser

# צילום מסך אוטומטי בטסטים שנכשלים
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        browser = item.funcargs.get("browser")
        if browser:
            screenshot = browser.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )


