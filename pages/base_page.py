import time
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    WebDriverException
)
from selenium.webdriver.common.by import By

class Base:
    def __init__(self, driver):
        self.driver: WebDriver = driver


    def safe_click(self, locator, timeout=10, wait_after_click=1.5):
        """
        לחיצה בטוחה על אלמנט:
        מנסה רגיל, ואם נכשל - לוחץ עם JavaScript.

        הערה חשובה:
        הפרמטר locator הוא טופל שלם (למשל: (By.ID, "some-id")),
        ואין צורך לפרק אותו כאן עם כוכבית.

        - לעומת זאת, כשקוראים ישירות לפונקציות של selenium כמו find_element,
  יש לפרק את הטופל עם כוכבית (*locator) כדי להעביר שני ארגומנטים נפרדים.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except (ElementClickInterceptedException, WebDriverException) as e:
            print(f"שגיאה בלחיצה רגילה: {e}. מנסה דרך JavaScript...")
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)

        if wait_after_click:
            time.sleep(wait_after_click)

    def safe_click_element(self, element, timeout=10, wait_after_click=1.5):
        """
        לחיצה בטוחה על WebElement שכבר קיים
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(element)
            )
            element.click()
        except (ElementClickInterceptedException, WebDriverException) as e:
            print(f"שגיאה בלחיצה רגילה: {e}. מנסה דרך JavaScript...")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)

        if wait_after_click:
            time.sleep(wait_after_click)

    def safe_send_keys(self, locator, text, timeout=10):
        """
        הכנסת טקסט לשדה לאחר המתנה שהוא נטען ונהיה לחיץ
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print(f"שגיאה: האלמנט לא נטען בזמן: {locator}")

    def get_element_text(self, locator, timeout=10):
        """
        מחזיר טקסט מתוך אלמנט, עם המתנה עד שהוא מופיע
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.text
        except TimeoutException:
            print(f"שגיאה: לא נמצא טקסט מהאלמנט: {locator}")
            return ""

