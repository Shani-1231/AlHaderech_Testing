import pytest
import allure
from pages.my_account import MyAccount

@pytest.mark.account
@allure.suite("My Account")
@allure.story("Update personal details")
@allure.severity(allure.severity_level.NORMAL)
def test_034_update_account_details(logged_in_user):
    page = MyAccount(logged_in_user)
    new_last_name = "כהן"
    page.open_my_account()
    page.change_account_details(new_last_name)
    assert page.change_success_message_is_displayed(), "הודעת 'פרטי החשבון שונו' לא מופיעה"
    assert page.get_last_name_value() == new_last_name, "שם המשפחה לא עודכן כמצופה"

@pytest.mark.account
@allure.suite("My Account")
@allure.story("Update shipping address")
@allure.severity(allure.severity_level.CRITICAL)
def test_035_update_address(logged_in_user):
    page = MyAccount(logged_in_user)
    new_city = "חולון"
    page.open_my_account()
    page.change_address(new_city)
    assert page.change_success_message_is_displayed(), "הודעת 'הכתובת שונתה' לא מופיעה"
    shipping_address = page.get_shipping_address()
    assert new_city in shipping_address, "העיר לא עודכנה בכתובת"

@pytest.mark.account
@allure.suite("My Account")
@allure.story("Logout process")
@allure.severity(allure.severity_level.NORMAL)
def test_036_logout_process(logged_in_user):
    page = MyAccount(logged_in_user)
    page.open_my_account()
    page.perform_logout()
    assert page.login_btn_is_displayed(), "כפתור ההתחברות לא מוצג בדף, נראה שההתנתקות לא בוצעה"

