import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Base

class MyAccount(Base):
    def __init__(self, driver):
        super().__init__(driver)

    MY_ACCOUNT_BTN = (By.XPATH, "(//span[@class='elementor-icon-list-text'])[1]")
    ACCOUNT_DETAILS_TAB = (By.XPATH, "//*[contains(@class,'edit-account')]")
    ADDRESSES_TAB = (By.XPATH, "//*[contains(@class,'edit-address')]")
    LOGOUT_BTN = (By.XPATH, "//*[contains(@class,'customer-logout')]")
    LAST_NAME = (By.CSS_SELECTOR, "#account_last_name")
    SAVE_DETAILS_BTN = (By.NAME, "save_account_details")
    CHANGE_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".woocommerce-message")
    EDIT_SHIPPING_ADDRESS_LINK = (By.XPATH, "//a[contains(.,'ערוך כתובת משלוח')]")
    SELECT_CITY = (By.ID, "select2-shipping_state-container")
    CITY_INPUT = (By.CLASS_NAME, "select2-search__field")
    SAVE_ADDRESS_BTN = (By.NAME, "save_address")
    SHIPPING_ADDRESS = (By.XPATH, "//*[contains(@class,'col-2')]//address")
    LOGIN_BTN = (By.NAME, "login")

    def open_my_account(self):
        self.safe_click(self.MY_ACCOUNT_BTN)

    def change_account_details(self, last_name):
        self.safe_click(self.ACCOUNT_DETAILS_TAB)
        self.safe_send_keys(self.LAST_NAME, last_name)
        self.safe_click(self.SAVE_DETAILS_BTN)

    def change_success_message_is_displayed(self):
        return self.driver.find_element(*self.CHANGE_SUCCESS_MESSAGE).is_displayed()

    def get_last_name_value(self):
        return self.driver.find_element(*self.LAST_NAME).get_attribute("value")

    def select_city_by_typing(self, city, timeout=10):
        """
        בחירת עיר מתוך תפריט select ע"י הקלדה
        """
        try:
            # מציאת אלמנט הסלקט
            select_element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.SELECT_CITY)
            )
            # גלילה אל האלמנט (אמצע המסך)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});",
                select_element
            )
            # לחיצה עם ActionChains
            ActionChains(self.driver).move_to_element(select_element).click().perform()
            # המתנה לשדה הקלט שמופיע לאחר הלחיצה
            input_field = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.CITY_INPUT)
            )
            # הכנסת שם העיר ולחיצה על Enter
            input_field.send_keys(city)
            input_field.send_keys(Keys.ENTER)
        except TimeoutException:
            print(f"שגיאה: שדה העיר לא היה מוכן בזמן")

    def change_address(self, city):
        self.safe_click(self.ADDRESSES_TAB)
        self.safe_click(self.EDIT_SHIPPING_ADDRESS_LINK)
        self.select_city_by_typing(city)
        self.safe_click(self.SAVE_ADDRESS_BTN)

    def get_shipping_address(self):
        return self.get_element_text(self.SHIPPING_ADDRESS)

    def perform_logout(self):
        """
        ניסיון התנתקות עם לחיצה "אמיתית" (ActionChains), לאחר גלילה.
        """
        try:
            logout_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.LOGOUT_BTN)
            )
            # גלילה למרכז המסך
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                       logout_btn)
            time.sleep(0.5)
            # ניסיון בלחיצה אמיתית עם ActionChains
            ActionChains(self.driver).move_to_element(logout_btn).pause(0.2).click().perform()
            time.sleep(1.5)
        except TimeoutException:
            print("⛔ כפתור ההתנתקות לא נמצא.")

    def login_btn_is_displayed(self, timeout=10):
        try:
            login_btn = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.LOGIN_BTN)
            )
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", login_btn)
            return login_btn.is_displayed()
        except TimeoutException:
            return False





