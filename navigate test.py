from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


def main():
    chrome_options = Options()
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    service = Service(r"C:\Users\salim\ChromeWebDriver\chromedriver-win64\chromedriver.exe")

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()

        driver.get("https://www.wildberries.ru/brands/kazakhstan")
        print("Navigated to Wildberries.")

        driver.implicitly_wait(10)

        driver.get("https://www.gmail.com")
        print("Navigated to Gmail.")


        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
        print("Gmail page loaded.")

        driver.back()
        print("Navigated back to Wildberries.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'driver' in locals():
            driver.quit()
            print("Browser closed.")


if __name__ == "__main__":
    main()
