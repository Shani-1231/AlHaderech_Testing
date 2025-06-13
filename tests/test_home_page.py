from pages.home_page import HomePage
import pytest

def test_004_homepage_loads_successfully(homepage):
    page = HomePage(homepage)
    assert page.logo_is_displayed(), "הלוגו לא מוצג בדף"
    assert page.menu_is_displayed(), "התפריט לא מוצג בדף"

def test_005_logo_is_displayed_and_loaded(homepage):
    page = HomePage(homepage)
    assert page.logo_is_displayed(), "הלוגו לא מוצג בדף"
    logo_src = page.get_logo_src()
    assert logo_src and logo_src.strip() != "", "src של הלוגו ריק, כנראה שהתמונה לא נטענה"

def test_006_logo_click_redirects_to_home(browser):
    page = HomePage(browser)
    browser.get("https://al-haderech.co.il/product-category/gifts/")
    page.click_logo()
    assert browser.current_url == "https://al-haderech.co.il/", "המעבר לעמוד הבית לא הצליח"

