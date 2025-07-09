import pytest
import allure
from pages.search import Search
from pages.cart_area import CartArea

@pytest.mark.cart
@allure.suite("Cart")
@allure.story("Empty cart")
@allure.severity(allure.severity_level.MINOR)
def test_025_cart_is_empty(logged_in_user):
    cart_page = CartArea(logged_in_user)
    cart_page.remove_all_items()
    qty = cart_page.get_cart_icon_qty()
    assert qty is not None, "לא הצליח ניסיון להוציא מספר על אייקון העגלה"
    assert qty == 0, "המספר 0 לא מופיע על אייקון העגלה"

@pytest.mark.cart
@allure.suite("Cart")
@allure.story("Add item to cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_026_add_item_to_cart(logged_in_user):
    cart_page = CartArea(logged_in_user)
    search_page = Search(logged_in_user)
    cart_page.remove_all_items()
    search_value = "זית"
    search_page.type_in_search_field(search_value)
    search_page.click_search_button()
    cart_page.add_item_by_index(1, expected_qty_after=1)
    assert cart_page.get_cart_icon_qty() == 1, "המספר על אייקון העגלה לא 1"
    cart_page.click_cart_icon()
    titles = cart_page.get_all_titles_in_cart()
    assert len(titles) == 1, f"מספר הפריטים בעגלה שונה מהמצופה, נמצאו {len(titles)}"
    assert titles[0] == "זית 10 ל'", "כותרת הפריט בעגלה שונה מהמצופה"
    price = cart_page.get_item_price_in_cart()
    assert price == "₪135.00"

@pytest.mark.cart
@allure.suite("Cart")
@allure.story("Remove item from cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_027_remove_item_from_cart(logged_in_user):
    cart_page = CartArea(logged_in_user)
    search_page = Search(logged_in_user)
    cart_page.remove_all_items()
    search_value = "זית"
    search_page.type_in_search_field(search_value)
    search_page.click_search_button()
    cart_page.add_item_by_index(1, expected_qty_after=1)
    assert cart_page.get_cart_icon_qty() == 1, "המספר 1 לא מופיע על אייקון העגלה"
    cart_page.remove_item()
    qty = cart_page.get_cart_icon_qty()
    assert qty == 0, "המספר 0 לא מופיע על אייקון העגלה"
    cart_page.click_cart_icon()
    titles = cart_page.get_all_titles_in_cart()
    assert titles == [], "העגלה לא ריקה כמצופה"




