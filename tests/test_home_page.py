import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.home_page import HomePage

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Homepage layout and UI elements")
@allure.severity(allure.severity_level.NORMAL)
def test_003_homepage_loads_successfully(homepage):
    page = HomePage(homepage)
    assert page.logo_is_displayed(), "הלוגו לא מוצג בדף"
    assert page.menu_is_displayed(), "התפריט הראשי לא מוצג בדף"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Homepage layout and UI elements")
@allure.severity(allure.severity_level.NORMAL)
def test_004_logo_is_displayed_and_loaded(homepage):
    page = HomePage(homepage)
    assert page.logo_is_displayed(), "הלוגו לא מוצג בדף"
    logo_src = page.get_logo_src()
    assert logo_src and logo_src.strip() != "", "src של הלוגו ריק, כנראה שהתמונה לא נטענה"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Logo navigation")
@allure.severity(allure.severity_level.CRITICAL)
def test_005_logo_click_redirects_to_homepage(browser):
    page = HomePage(browser)
    browser.get("https://al-haderech.co.il/product-category/gifts/")
    page.click_logo()
    assert browser.current_url == "https://al-haderech.co.il/", "המעבר לעמוד הבית לא הצליח"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Homepage layout and UI elements")
@allure.severity(allure.severity_level.MINOR)
def test_006_elements_are_displayed_in_top_bar(homepage):
    page = HomePage(homepage)
    assert page.top_bar_is_displayed(), "הסרגל העליון לא מוצג"
    assert page.get_my_account_text() == "החשבון שלי", "הטקסט 'החשבון שלי' לא מוצג"
    assert "03-9550043" in page.get_phone_number(), "מספר הטלפון לא נכון או לא מוצג"
    assert "יעקב פריימן, ראשון לציון" in page.get_store_address_text(), "הכתובת לא נכונה או לא מוצגת"
    assert page.shopping_cart_icon_is_displayed(), "אייקון עגלת הקניות לא מוצג"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Homepage layout and UI elements")
@allure.severity(allure.severity_level.NORMAL)
def test_008_key_categories_are_in_the_menu(homepage):
    page = HomePage(homepage)
    assert page.menu_is_displayed(), "התפריט הראשי לא מוצג בדף"
    categories_titles = page.get_menu_categories_titles()
    assert len(categories_titles) >= 8, "פחות מ-8 פריטים מופיעים בתפריט הראשי"
    expected_categories = ["מתנות", "פרחים טריים", "צמחים"]
    for category in expected_categories:
        assert category in categories_titles, f"הקטגוריה '{category}' לא מופיעה בתפריט הראשי"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Main menu interaction")
@allure.severity(allure.severity_level.NORMAL)
def test_009_hovering_over_menu_item(homepage):
    page = HomePage(homepage)
    assert page.get_flowers_submenu_visibility() == "hidden", "תת תפריט 'פרחים' כבר מוצג בהתחלה"
    page.hover_over_flowers_menu()
    WebDriverWait(page.driver, 5).until(
        lambda d: page.get_flowers_submenu_visibility() == "visible"
    )
    assert page.get_flowers_submenu_visibility() == "visible","תת תפריט 'פרחים' לא הופיע לאחר ריחוף"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Main menu interaction")
@allure.severity(allure.severity_level.CRITICAL)
def test_010_clicking_a_main_category(homepage):
    page = HomePage(homepage)
    page.click_plants_item()
    assert homepage.current_url == "https://al-haderech.co.il/product-category/%d7%a6%d7%9e%d7%97%d7%99%d7%9d/", "הכתובת לא מתאימה לעמוד הקטגוריה"
    assert "צמחים" in homepage.title, "כותרת העמוד לא מתאימה לקטגוריה שנבחרה"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Main menu interaction")
@allure.severity(allure.severity_level.CRITICAL)
def test_011_clicking_a_submenu_item(homepage):
    page = HomePage(homepage)
    page.hover_over_gardening_accessories_menu()
    page.click_irrigation_products_item()
    assert homepage.current_url == "https://al-haderech.co.il/product-category/%d7%90%d7%91%d7%99%d7%96%d7%a8%d7%99-%d7%92%d7%99%d7%a0%d7%95%d7%9f/%d7%9e%d7%95%d7%a6%d7%a8%d7%99-%d7%94%d7%a9%d7%a7%d7%99%d7%99%d7%94/", "הכתובת לא מתאימה לעמוד התת קטגוריה"
    assert "מוצרי השקייה" in homepage.title, "כותרת העמוד לא מתאימה לתת הקטגוריה שנבחרה"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Footer layout")
@allure.severity(allure.severity_level.MINOR)
def test_012_elements_are_displayed_in_footer(homepage):
    page = HomePage(homepage)
    page.scroll_down_the_page()
    assert page.footer_is_displayed(), "הפוטר לא מוצג לאחר גלילה לתחתית הדף"
    actual_titles = page.get_footer_titles()
    expected_titles = ['קניה משתלמת', 'מפת האתר', 'קטגוריות ראשיות', 'מידע', 'חפשו אותנו']
    for title in expected_titles:
        assert title in actual_titles, f"הכותרת '{title}' לא נמצאה בפוטר"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Footer links")
@allure.severity(allure.severity_level.NORMAL)
def test_013_clicking_about_us_link_in_footer(homepage):
    page = HomePage(homepage)
    page.click_about_us_link()
    assert homepage.current_url == "https://al-haderech.co.il/about/", "הכתובת לא מתאימה לעמוד האודות"
    assert "אודות" in homepage.title, "כותרת העמוד לא מתאימה ל'אודות'"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Footer external links")
@allure.severity(allure.severity_level.NORMAL)
def test_014_clicking_instagram_icon_in_footer(homepage):
    page = HomePage(homepage)
    page.open_instagram_page()
    assert homepage.current_url == "https://www.instagram.com/al_haderech_nursery/", "הכתובת של הטאב שנפתח לא מתאימה לעמוד האינסטגרם של האתר"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Accessibility features")
@allure.severity(allure.severity_level.NORMAL)
def test_015_clicking_accessibility_button(homepage):
    page = HomePage(homepage)
    page.click_accessibility_btn()
    assert page.accessibility_toolbar_is_displayed(), "תפריט הנגישות לא נפתח"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Join club button")
@allure.severity(allure.severity_level.MINOR)
def test_016_text_of_join_club_button(homepage):
    page = HomePage(homepage)
    assert "הצטרפו למועדון" in page.get_join_club_btn_text(), "הטקטסט של כפתור הצטרפות למועדון לא מוצג"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Join club button")
@allure.severity(allure.severity_level.CRITICAL)
def test_016_text_of_join_club_button(homepage):
    page = HomePage(homepage)
    page.click_join_club_btn()
    assert homepage.current_url == "https://al-haderech.co.il/items/%d7%97%d7%91%d7%a8%d7%95%d7%aa-%d7%91%d7%9e%d7%95%d7%a2%d7%93%d7%95%d7%9f-%d7%94%d7%9c%d7%a7%d7%95%d7%97%d7%95%d7%aa/", "הכתובת לא מתאימה לעמוד הצטרפות למועדון"
    assert "מועדון הלקוחות" in homepage.title, "כותרת העמוד לא מתאימה לעמוד 'הצטרפות למועדון'"

@pytest.mark.homepage
@allure.suite("Homepage")
@allure.story("Layout direction and language")
@allure.severity(allure.severity_level.NORMAL)
def test_018_layout_rtl_and_lang(homepage):
    page = HomePage(homepage)
    assert page.get_html_dir() == "rtl", "הכיווניות לא מוגדרת מימין לשמאל (rtl)"
    assert page.get_html_lang() == "he-IL", "השפה לא מוגדרת כעברית (he-IL)"



