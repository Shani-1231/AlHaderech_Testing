import pytest
import allure
from pages.search import Search

@pytest.mark.search
@allure.suite("Search")
@allure.story("Search field visibility and state")
@allure.severity(allure.severity_level.NORMAL)
def test_019_search_field_is_displayed(homepage):
    page = Search(homepage)
    search_input = page.get_search_input()
    assert search_input.is_displayed(), "שדה החיפוש לא מוצג"
    assert search_input.is_enabled(), "שדה החיפוש אינו פעיל להזנה"
    assert search_input.get_attribute("placeholder") == "מה אתם מחפשים?" , "טקסט הפלייסהולדר שגוי"

@pytest.mark.search
@allure.suite("Search")
@allure.story("Search input behavior")
@allure.severity(allure.severity_level.NORMAL)
def test_020_search_input_reflects_user_typing(homepage):
    page = Search(homepage)
    search_value = "בדיקת קלט"
    page.type_in_search_field(search_value)
    assert page.typed_value() == search_value, "הטקסט שהוקלד לא מופיע"

@pytest.mark.search
@allure.suite("Search")
@allure.story("Empty search behavior")
@allure.severity(allure.severity_level.NORMAL)
def test_021_no_action_when_search_field_is_empty(homepage):
    page = Search(homepage)
    page.clear_search_field()
    page.click_search_button()
    assert homepage.current_url == "https://al-haderech.co.il/", "נכשל: לאחר חיפוש עם שדה ריק, הכתובת לא נשארה עמוד הבית כמצופה"

@pytest.mark.search
@allure.suite("Search")
@allure.story("Valid search with button")
@allure.severity(allure.severity_level.CRITICAL)
def test_022_search_valid_input_with_button(homepage):
    page = Search(homepage)
    search_value = "ברוש"
    page.type_in_search_field(search_value)
    page.click_search_button()
    print("URL after search:", homepage.current_url)
    assert homepage.current_url != "https://al-haderech.co.il/", "הכתובת נשארה עמוד הבית, ולא עמוד תוצאות חיפוש"
    titles = page.get_results_titles()
    print("Number of results:", len(titles))
    assert len(titles) > 0, "לא נמצאו תוצאות חיפוש"
    matching_results = [title for title in titles if search_value.lower() in title.lower()]
    assert len(matching_results) > 0, "לא נמצאה אף תוצאה רלוונטית למילת החיפוש"

@pytest.mark.search
@allure.suite("Search")
@allure.story("Valid search with Enter key")
@allure.severity(allure.severity_level.CRITICAL)
def test_023_search_valid_input_with_enter(homepage):
    page = Search(homepage)
    search_value = "ברוש"
    page.type_in_search_field(search_value)
    page.click_enter()
    print("URL after search:", homepage.current_url)
    assert homepage.current_url != "https://al-haderech.co.il/", "הכתובת נשארה עמוד הבית, ולא עמוד תוצאות חיפוש"
    titles = page.get_results_titles()
    print("Number of results:", len(titles))
    assert len(titles) > 0, "לא נמצאו תוצאות חיפוש"
    matching_results = [title for title in titles if search_value.lower() in title.lower()]
    assert len(matching_results) > 0, "לא נמצאה אף תוצאה רלוונטית למילת החיפוש"

@pytest.mark.search
@allure.suite("Search")
@allure.story("Search with no matching results")
@allure.severity(allure.severity_level.NORMAL)
def test_024_search_invalid_input_shows_no_results(homepage):
    page = Search(homepage)
    invalid_input = "aa1122"
    page.type_in_search_field(invalid_input)
    page.click_search_button()
    assert homepage.current_url != "https://al-haderech.co.il/", "הכתובת נשארה עמוד הבית, ולא עמוד- לא נמצאו מוצרים"
    no_results_message = page.get_no_results_message()
    assert "לא נמצאו מוצרים" in no_results_message, "לא מופיעה ההודעה:'לא נמצאו מוצרים' "









