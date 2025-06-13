from pages.base_page import Base
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

class Search(Base):
    def __init__(self, driver):
        super().__init__(driver)

    SEARCH_FIELD = (By.ID, "search-input-d07fac2")
    SEARCH_BTN = (By.XPATH, "//i[@class='fas fa-search']")
    SEARCH_RESULTS = (By.XPATH, "//h2[@class='woocommerce-loop-product__title']")


    def get_search_input(self):
        return self.driver.find_element(*self.SEARCH_FIELD)

    def type_in_search_field(self, search_input):
        self.safe_send_keys(self.SEARCH_FIELD, text= search_input)

    def typed_value(self):
        return self.driver.find_element(*self.SEARCH_FIELD).get_attribute("value")

    def clear_the_search_field(self):
        self.driver.find_element(*self.SEARCH_FIELD).clear()

    def click_the_search_button(self):
        self.safe_click(self.SEARCH_BTN)

    def search_results(self):
        return self.driver.find_elements(*self.SEARCH_RESULTS)

    def get_results_titles(self):
        elements = self.search_results()
        return [el.text for el in elements]
