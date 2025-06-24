import json
import os
import pytest
import allure
from pages.login import Login

@pytest.mark.account
@allure.suite("Login")
@allure.story("Successful login with valid credentials")
@allure.severity(allure.severity_level.BLOCKER)
def test_001_correct_login(logged_out_user):
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")
    with open(config_path) as f:
        creds = json.load(f)
    username = creds["username"]
    password = creds["password"]

    page = Login(logged_out_user)
    page.click_my_account_btn()
    page.perform_login(username, password)
    greeting_text = page.get_greeting_text()
    assert "שלום" in greeting_text, "לא התקבלה הודעת ברכה אחרי ההתחברות"

@pytest.mark.account
@allure.suite("Login")
@allure.story("Login attempt with incorrect password")
@allure.severity(allure.severity_level.CRITICAL)
def test_002_incorrect_login(logged_out_user):
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")
    with open(config_path) as f:
        creds = json.load(f)
    username = creds["username"]
    wrong_password = "abcd1234"

    page = Login(logged_out_user)
    page.click_my_account_btn()
    page.perform_login(username, wrong_password)
    assert page.error_message_is_displayed(), "הודעת השגיאה לא הופיעה כמצופה"


