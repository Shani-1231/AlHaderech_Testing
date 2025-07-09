from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Base


class CartArea(Base):
    def __init__(self, driver):
        super().__init__(driver)

    ADD_TO_CART_BUTTONS = (By.XPATH, "(//a[contains(@class,'ajax')])")
    CART_ICON = (By.CLASS_NAME, "eicon-cart-medium")
    CART_ICON_QTY = (By.CLASS_NAME, "elementor-button-icon-qty")
    REMOVE_BTN = (By.CLASS_NAME, "remove_from_cart_button")
    CLOSE_MINI_CART_BTN = (By.CLASS_NAME, "elementor-menu-cart__close-button")
    TITLES_ITEMS_IN_CART = (By.XPATH, "//div[@class='ast-product-name']/a")
    FULL_CART_BTN = (By.XPATH, "//span[contains(.,'סל הקניות')]")
    Q2Y_PLUS_BTN = (By.CLASS_NAME, "plus")
    UPDATE_CART_BTN = (By.NAME, "update_cart")
    PRICE_ITEMS_IN_CART = (By.XPATH, "//div[contains(@class,'mini-cart-price')]/span[contains(@class,'Price-amount')]")
    TOTAL_PRICE_MINI_CART = (By.XPATH, "//div[contains(@class,'cart__subtotal')]/span[contains(@class,'Price-amount')]")

    def remove_all_items(self):
        self.safe_click(self.CART_ICON)
        # בדיקה מוקדמת: אם אין כפתור מחיקה – אין מה למחוק
        if not self.is_element_present(self.REMOVE_BTN):
            self.safe_click(self.CLOSE_MINI_CART_BTN)
            return
        try:
            while True:
                # ממתינים שהכפתור יופיע ב-DOM
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(self.REMOVE_BTN)
                )
                # לחיצה עם JavaScript כדי להימנע מ-stale
                self.driver.execute_script(
                    "arguments[0].click();",
                    self.driver.find_element(*self.REMOVE_BTN)
                )
                # המתנה שהכפתור ייעלם (כלומר שהפריט נמחק)
                WebDriverWait(self.driver, 5).until(
                    EC.staleness_of(self.driver.find_element(*self.REMOVE_BTN))
                )
        except Exception:
            # כשאין יותר פריטים – תיזרק שגיאה ונצא מהלולאה
            pass
        self.safe_click(self.CLOSE_MINI_CART_BTN)

    def get_cart_icon_qty(self):
        text_qty = self.get_element_text(self.CART_ICON_QTY).strip()
        try:
            return int(text_qty)
        except ValueError:
            return None

    def click_cart_icon(self):
        self.safe_click(self.CART_ICON)

    def wait_for_cart_icon_qty(self, expected_qty, timeout=5):
        WebDriverWait(self.driver, timeout).until(lambda d: self.get_cart_icon_qty() == expected_qty,
            f"Cart icon quantity did not reach {expected_qty} within {timeout} seconds")

    def add_item_by_index(self, index, expected_qty_after=None):
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if index >= len(add_buttons):
            raise IndexError(f"Only {len(add_buttons)} 'add to cart' buttons found, but tried to access index {index}")
        self.safe_click_element(add_buttons[index])
        if expected_qty_after is not None:
            self.wait_for_cart_icon_qty(expected_qty_after)

    def get_all_titles_in_cart(self):
        elements = self.driver.find_elements(*self.TITLES_ITEMS_IN_CART)
        return [el.text.strip() for el in elements if el.text.strip() and el.is_displayed()]

    def get_item_price_in_cart(self):
        return self.get_element_text(self.PRICE_ITEMS_IN_CART)

    def get_all_prices_in_cart(self):
        elements = self.driver.find_elements(*self.PRICE_ITEMS_IN_CART)
        return [el.text.strip() for el in elements if el.text.strip() and el.is_displayed()]

    def get_total_price_in_cart(self):
        return self.get_element_text(self.TOTAL_PRICE_MINI_CART).strip()

    def remove_item(self):
        self.safe_click(self.CART_ICON)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.REMOVE_BTN))
            self.driver.execute_script(
                "arguments[0].click();",
                self.driver.find_element(*self.REMOVE_BTN)
            )
            # המתנה שהכפתור ייעלם (כלומר שהפריט יוסר)
            WebDriverWait(self.driver, 5).until(EC.staleness_of(self.driver.find_element(*self.REMOVE_BTN)))
            print("הפריט הוסר בהצלחה.")
        except Exception as e:
            print(f"שגיאה במחיקת פריט מהעגלה: {e}")
        finally:
            self.safe_click(self.CLOSE_MINI_CART_BTN)












