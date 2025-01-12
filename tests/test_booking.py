import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.search_page import FlightReservationPage

class FlightReservationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service = Service(r"C:\Users\salim\ChromeWebDriver\chromedriver-win64\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.page = FlightReservationPage(cls.driver)

    def test_make_flight_reservation_using_pom(self):
        try:
            # Arrange
            self.page.navigate_to("https://aviata.kz")

            # Act
            self.page.enter_from_where_and_select_suggestion("Астана")
            self.page.enter_to_where_and_select_suggestion("Петропавловск")
            self.page.click_search_button()

            # Retrieve buttons and assert
            choose_buttons = self.page.get_choose_buttons()
            with self.assertRaises(IndexError):
                choose_buttons[0].click()

        except Exception as e:
            self.fail(f"Test failed with exception: {e}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
