import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import Base


class Search(Base):
    def __init__(self, driver):
        super().__init__(driver)

    SEARCH_FIELD = (By.ID, "search-input-d07fac2")
    SEARCH_BTN = (By.XPATH, "//i[@class='fas fa-search']")
    SEARCH_RESULTS = (By.XPATH, "//h2[@class='woocommerce-loop-product__title']")
    NO_RESULTS_MESSAGE = (By.CLASS_NAME, "woocommerce-info")


    def get_search_input(self):
        return self.driver.find_element(*self.SEARCH_FIELD)

    def type_in_search_field(self, search_input):
        self.safe_send_keys(self.SEARCH_FIELD, text= search_input)

    def typed_value(self):
        return self.driver.find_element(*self.SEARCH_FIELD).get_attribute("value")

    def clear_search_field(self):
        self.driver.find_element(*self.SEARCH_FIELD).clear()

    def click_search_button(self):
        self.safe_click(self.SEARCH_BTN)

    def click_enter(self):
        self.driver.find_element(*self.SEARCH_FIELD).send_keys(Keys.ENTER)
        time.sleep(1.5)

    def get_results_titles(self):
        elements = self.driver.find_elements(*self.SEARCH_RESULTS)
        return [el.text for el in elements]

    def get_no_results_message(self):
        no_results_message = self.get_element_text(self.NO_RESULTS_MESSAGE)
        return no_results_message

