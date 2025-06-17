import time
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from pages.base_page import Base

class HomePage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    LOGO = (By.XPATH, "//img[@alt='משתלת על הדרך']")
    MENU = (By.CLASS_NAME, "jet-menu-inner")
    TOP_MENU_ITEMS = (By.CSS_SELECTOR, ".jet-menu > li > a.top-level-link")
    SUB_MENU_ITEMS = (By.CSS_SELECTOR, ".jet-sub-menu li a")

    # דוגמה: קריאה לפונקציית selenium עם פירוק טאפל
    # element = self.driver.find_element(*locator)
    def logo_is_displayed(self):
        return self.driver.find_element(*self.LOGO).is_displayed()

    def menu_is_displayed(self):
        return self.driver.find_element(*self.MENU).is_displayed()

    def get_logo_src(self):
        return self.driver.find_element(*self.LOGO).get_attribute("src")

    def click_logo(self):
        self.safe_click(self.LOGO)


