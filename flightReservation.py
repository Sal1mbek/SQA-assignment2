from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class FlightReservationTests(unittest.TestCase):
    def setUp(self):
        """Setup the Chrome WebDriver."""
        self.driver = webdriver.Chrome()

    def test_make_flight_reservation_using_css_selectors(self):
        """Test flight booking functionality using CSS Selectors."""
        driver = self.driver
        # Arrange
        driver.get("https://aviata.kz")

        # Find elements using CSS Selectors
        from_where = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Откуда']")
        where_to = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Куда']")
        search_button = driver.find_element(By.CSS_SELECTOR, "button.search-form__btn")

        # Act
        from_where.click()
        from_where.send_keys("Астана")
        time.sleep(3)
        suggestion1 = driver.find_element(By.CSS_SELECTOR, ".border-b")
        suggestion1.click()

        where_to.click()
        where_to.send_keys("Алматы")
        time.sleep(3)
        suggestion2 = driver.find_element(By.CSS_SELECTOR, ".border-b")
        suggestion2.click()

        search_button.click()
        time.sleep(3)

        # Assert title contains expected location
        self.assertIn("Астана", driver.title)
        self.assertIn("Алматы", driver.title)

    def test_make_flight_reservation_using_xpath(self):
        """Test flight booking functionality using XPath."""
        driver = self.driver
        # Arrange
        driver.get("https://aviata.kz")

        # Find elements using XPath
        from_where = driver.find_element(By.XPATH, "//input[@placeholder='Откуда']")
        where_to = driver.find_element(By.XPATH, "//input[@placeholder='Куда']")
        search_button = driver.find_element(By.XPATH, "//button[contains(@class, 'search-form__btn')]")

        # Act
        from_where.click()
        from_where.send_keys("Астана")
        time.sleep(2)
        suggestion1 = driver.find_element(By.XPATH, "//div[contains(@class, 'border-b')]")
        suggestion1.click()

        where_to.click()
        where_to.send_keys("Алматы")
        time.sleep(2)
        suggestion2 = driver.find_element(By.XPATH, "//div[contains(@class, 'border-b')]")
        suggestion2.click()

        search_button.click()
        time.sleep(3)

        # Assert title contains expected location
        self.assertIn("Астана", driver.title)
        self.assertIn("Алматы", driver.title)

    def tearDown(self):
        """Clean up the WebDriver."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
