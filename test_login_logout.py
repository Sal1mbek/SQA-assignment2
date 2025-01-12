import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class LoginAndLogoutFunctionalityTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        with open("UserData.json", "r") as file:
            self.user_data = json.load(file)

    def test_login_and_logout_using_css_selector(self):
        driver = self.driver
        # Arrange
        driver.get("https://saucedemo.com")
        username_field = driver.find_element(By.CSS_SELECTOR, "input#user-name")
        password_field = driver.find_element(By.CSS_SELECTOR, "input#password")
        login_button = driver.find_element(By.CSS_SELECTOR, "input#login-button")

        # Act
        username_field.send_keys(self.user_data["Username"])
        password_field.send_keys(self.user_data["Password"])
        login_button.click()

        # Wait until redirected to the inventory page
        WebDriverWait(driver, 3).until(EC.url_contains("inventory.html"))

        # Assert successful login
        self.assertIn("saucedemo.com/inventory.html", driver.current_url)

        # Perform logout
        menu_icon = driver.find_element(By.CSS_SELECTOR, "button#react-burger-menu-btn")
        menu_icon.click()
        logout_button = driver.find_element(By.CSS_SELECTOR, "a#logout_sidebar_link")
        logout_button.click()

        # Wait until login button is visible
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input#login-button"))
        )
        login_button_after_logout = driver.find_element(By.CSS_SELECTOR, "input#login-button")

        # Assert successful logout
        self.assertIsNotNone(login_button_after_logout)

    def test_login_and_logout_using_xpath(self):
        driver = self.driver
        # Arrange
        driver.get("https://saucedemo.com")
        username_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
        password_field = driver.find_element(By.XPATH, "//input[@id='password']")
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")

        # Act
        username_field.send_keys(self.user_data["Username"])
        password_field.send_keys(self.user_data["Password"])
        login_button.click()

        # Wait until redirected to the inventory page
        WebDriverWait(driver, 3).until(EC.url_contains("inventory.html"))

        # Assert successful login
        self.assertIn("saucedemo.com/inventory.html", driver.current_url)

        # Perform logout
        menu_icon = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
        menu_icon.click()
        logout_button = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
        logout_button.click()

        # Wait until login button is visible
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='login-button']"))
        )
        login_button_after_logout = driver.find_element(By.XPATH, "//input[@id='login-button']")

        # Assert successful logout
        self.assertIsNotNone(login_button_after_logout)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
