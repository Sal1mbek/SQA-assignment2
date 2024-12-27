from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class SearchFunctionalityTests(unittest.TestCase):
    def setUp(self):
        """Setup the Chrome WebDriver."""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)  # Implicit wait for locating elements.

    def test_search_by_user_imitation_using_css_selector(self):
        """Test search functionality using CSS Selector."""
        driver = self.driver
        # Arrange
        driver.get("https://www.google.com")
        search_bar = driver.find_element(By.CSS_SELECTOR, "textarea#APjFqb")

        # Act
        search_bar.send_keys("Quality Assurance")
        search_bar.send_keys(Keys.ENTER)

        # Wait until title contains the search query
        WebDriverWait(driver, 3).until(EC.title_contains("Quality Assurance"))

        # Assert
        self.assertIn("Quality Assurance", driver.title)

    def test_search_by_user_imitation_using_xpath(self):
        """Test search functionality using XPath."""
        driver = self.driver
        # Arrange
        driver.get("https://www.google.com")
        search_bar = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")

        # Act
        search_bar.send_keys("Quality Assurance")
        search_bar.send_keys(Keys.ENTER)

        # Wait until title contains the search query
        WebDriverWait(driver, 3).until(EC.title_contains("Quality Assurance"))

        # Assert
        self.assertIn("Quality Assurance", driver.title)

    def test_search_by_changing_url_contents(self):
        """Test search functionality by modifying the URL."""
        driver = self.driver
        # Arrange
        driver.get("https://www.google.com")
        topic_to_search = "Quality+Assurance"

        # Act
        driver.get(f"https://www.google.com/search?q={topic_to_search}")

        # Wait until title contains the search query
        WebDriverWait(driver, 3).until(EC.title_contains("Quality Assurance"))

        # Assert
        self.assertIn("Quality Assurance", driver.title)
        self.assertIn("Quality+Assurance", driver.current_url)

    def tearDown(self):
        """Clean up the WebDriver."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
