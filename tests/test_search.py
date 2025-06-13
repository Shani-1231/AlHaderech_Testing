import pytest
from pages.search import Search

def test_015_search_field_is_displayed(homepage):
    page = Search(homepage)
    search_input = page.get_search_input()
    assert search_input.is_displayed(), "שדה החיפוש לא מוצג"
    assert search_input.is_enabled(), "שדה החיפוש אינו פעיל להזנה"
    assert search_input.get_attribute("placeholder") == "מה אתם מחפשים?" , "טקסט הפלייסהולדר שגוי"

def test_003_search_input_reflects_user_typing(homepage):
    page = Search(homepage)
    search_value = "בדיקת קלט"
    page.type_in_search_field(search_value)
    assert page.typed_value() == search_value, "הטקסט שהוקלד לא מופיע"

def test_016_no_action_when_search_field_is_empty(homepage):
    page = Search(homepage)
    page.clear_the_search_field()
    page.click_the_search_button()
    assert homepage.current_url == "https://al-haderech.co.il/", "נכשל: לאחר חיפוש עם שדה ריק, הכתובת לא נשארה עמוד הבית כמצופה"

def test_017_search_returns_relevant_results_for_valid_query(homepage):
    page = Search(homepage)
    search_value = "ברוש"
    page.type_in_search_field(search_value)
    page.click_the_search_button()
    print("URL after search:", homepage.current_url)
    assert homepage.current_url != "https://al-haderech.co.il/", "הכתובת נשארה עמוד הבית, ולא עמוד תוצאות חיפוש"
    titles = page.get_results_titles()
    print("Number of results:", len(titles))
    assert len(titles) > 0, "לא נמצאו תוצאות חיפוש"
    matching_results = [title for title in titles if search_value.lower() in title.lower()]
    assert len(matching_results) > 0, "לא נמצאה אף תוצאה רלוונטית למילת החיפוש"







