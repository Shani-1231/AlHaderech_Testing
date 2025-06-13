import json
import os
import pytest
from pages.login import Login

def test_001_incorrect_login(homepage):
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")
    with open(config_path) as f:
        creds = json.load(f)
    username = creds["username"]
    wrong_password = "abcd1234"

    page = Login(homepage)
    page.click_my_account_btn()
    page.perform_login(username, wrong_password)
    assert page.error_message_is_displayed(), "הודעת השגיאה לא הופיעה כמצופה"

def test_002_correct_login(homepage):
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")
    with open(config_path) as f:
        creds = json.load(f)
    username = creds["username"]
    password = creds["password"]

    page = Login(homepage)
    page.click_my_account_btn()
    page.perform_login(username, password)
    greeting_text = page.get_greeting_text()
    assert "שלום" in greeting_text, "לא התקבלה הודעת ברכה אחרי ההתחברות"
