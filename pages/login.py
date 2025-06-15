import time
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import Base

class Login(Base):
    def __init__(self, driver):
        super().__init__(driver)

    MY_ACCOUNT_BTN = (By.XPATH, "(//span[@class='elementor-icon-list-text'])[1]")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.NAME, "login")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='ttt-pnwc-message']")
    GREETING_MESSAGE = (By.XPATH, "(//p[@data-fontsize])[1]")

    def click_my_account_btn(self):
        self.safe_click(self.MY_ACCOUNT_BTN)

    def perform_login(self, username, password):
        self.safe_send_keys(self.USERNAME, username)
        self.safe_send_keys(self.PASSWORD, password)
        self.safe_click(self.LOGIN_BTN)

    def error_message_is_displayed(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).is_displayed()

    def get_greeting_text(self):
        try:
            return self.driver.find_element(*self.GREETING_MESSAGE).text
        except NoSuchElementException:
            return ""



