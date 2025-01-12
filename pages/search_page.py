from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FlightReservationPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    FROM_WHERE_FIELD = (By.CSS_SELECTOR, "input[placeholder='Откуда']")
    TO_WHERE_FIELD = (By.CSS_SELECTOR, "input[placeholder='Куда']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-form__btn")
    SUGGESTION = (By.CSS_SELECTOR, ".border-b")

    def navigate_to(self, url):
        self.driver.get(url)

    def enter_from_where_and_select_suggestion(self, location):
        from_field = self.driver.find_element(*self.FROM_WHERE_FIELD)
        from_field.click()
        from_field.send_keys(location)
        time.sleep(2)
        self.wait_for_suggestions_and_select()

    def enter_to_where_and_select_suggestion(self, location):
        to_field = self.driver.find_element(*self.TO_WHERE_FIELD)
        to_field.click()
        to_field.send_keys(location)
        time.sleep(2)
        self.wait_for_suggestions_and_select()

    def wait_for_suggestions_and_select(self):
        wait = WebDriverWait(self.driver, 10)
        suggestion = wait.until(
            EC.element_to_be_clickable(self.SUGGESTION)
        )
        self.driver.execute_script("arguments[0].click();", suggestion)

    def click_search_button(self):
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def get_choose_buttons(self):
        return self.driver.find_elements(*self.SEARCH_BUTTON)
