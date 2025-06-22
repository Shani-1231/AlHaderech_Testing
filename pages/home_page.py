import time
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Base

class HomePage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    LOGO = (By.XPATH, "//img[@alt='משתלת על הדרך']")
    MENU = (By.CLASS_NAME, "jet-menu-inner")
    TOP_BAR = (By.CSS_SELECTOR, "div[data-id='390f92a']")
    MY_ACCOUNT_LINK = (By.XPATH, "(//span[@class='elementor-icon-list-text'])[1]")
    PHONE_NUMBER = (By.XPATH, "(//a[@href='tel:03-9550043'])[2]")
    STORE_ADDRESS = (By.XPATH, "(//div[@class='elementor-image-box-title'])[2]")
    SHOPPING_CART_ICON = (By.CLASS_NAME, "eicon-cart-medium")
    TOP_MENU_ITEMS = (By.CSS_SELECTOR, ".jet-menu > li > a.top-level-link")
    SUB_MENU_ITEMS = (By.CSS_SELECTOR, ".jet-sub-menu li a")
    FLOWERS_ITEM = (By.ID, "jet-menu-item-313")
    FLOWERS_SUB_MENU = (By.XPATH, "//div[@data-id='edd0d03']")
    PLANTS_ITEM = (By.ID, "jet-menu-item-319")
    GARDENING_ACCESSORIES_ITEM = (By.ID, "jet-menu-item-292")
    IRRIGATION_PRODUCTS_ITEM = (By.XPATH, "(//div[@data-id='df6cf0d']//a)[1]")
    FOOTER = (By.XPATH, "//section[@data-id='74e27025']")
    FOOTER_TITLES = (By.TAG_NAME, "h4")
    ABOUT_US_LINK = (By.XPATH, "(//div[@data-id='c4ebfab']//a)[1]")
    INSTAGRAM_ICON = (By.CSS_SELECTOR, ".fa-instagram")


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

    def top_bar_is_displayed(self):
        return self.driver.find_element(*self.TOP_BAR).is_displayed()

    def get_my_account_text(self):
       return self.get_element_text(self.MY_ACCOUNT_LINK)

    def get_phone_number(self):
       return self.get_element_text(self.PHONE_NUMBER)

    def get_store_address_text(self):
        return self.get_element_text(self.STORE_ADDRESS)

    def shopping_cart_icon_is_displayed(self):
        return self.driver.find_element(*self.SHOPPING_CART_ICON).is_displayed()

    def get_menu_categories_titles(self):
        elements = self.driver.find_elements(*self.TOP_MENU_ITEMS)
        return [el.text for el in elements]

    def get_flowers_submenu_visibility(self):
        submenu = self.driver.find_element(*self.FLOWERS_SUB_MENU)
        return submenu.value_of_css_property("visibility")

    def hover_over_flowers_menu(self):
        menu_item = self.driver.find_element(*self.FLOWERS_ITEM)
        action = ActionChains(self.driver)
        action.move_to_element(menu_item).perform()

    def click_plants_item(self):
        self.safe_click(self.PLANTS_ITEM)

    def hover_over_gardening_accessories_menu(self):
        menu_item = self.driver.find_element(*self.GARDENING_ACCESSORIES_ITEM)
        action = ActionChains(self.driver)
        action.move_to_element(menu_item).perform()

    def click_irrigation_products_item(self):
        self.safe_click(self.IRRIGATION_PRODUCTS_ITEM)

    def scroll_down_the_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def footer_is_displayed(self):
        return self.driver.find_element(*self.FOOTER).is_displayed()

    def get_footer_titles(self):
        titles = self.driver.find_elements(*self.FOOTER_TITLES)
        return [t.text.strip() for t in titles]

    def click_about_us_link(self):
        self.safe_click(self.ABOUT_US_LINK)

    def open_instagram_page(self):
        self.safe_click(self.INSTAGRAM_ICON)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])


    def get_html_dir(self):
        return self.driver.execute_script("return document.documentElement.getAttribute('dir')")

    def get_html_lang(self):
        return self.driver.execute_script("return document.documentElement.getAttribute('lang')")


