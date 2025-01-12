import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

# Define service for ChromeDriver
service = Service(r"C:\Users\salim\ChromeWebDriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://demoqa.com/")
    driver.maximize_window()

    print("Test Report:\n")

    # Implement Implicit Wait
    driver.implicitly_wait(10)
    print("1. Implicit Wait - passed")

    # Navigate to the Forms page
    driver.find_element(By.XPATH, "//h5[text()='Forms']").click()

    # Implement Explicit Wait
    explicit_wait = WebDriverWait(driver, 10)
    practice_form = explicit_wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Practice Form']")))
    practice_form.click()
    print("2. Explicit Wait - passed")

    # Implement Fluent Wait
    fluent_wait = WebDriverWait(driver, timeout=15, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
    fluent_element = fluent_wait.until(EC.presence_of_element_located((By.ID, "firstName")))
    print("3. Fluent Wait - passed")

    # Enter data into the form
    fluent_element.send_keys("Salimbek")
    driver.find_element(By.ID, "lastName").send_keys("Kairbekov")
    driver.find_element(By.ID, "userEmail").send_keys("testemail@example.com")

    # Implement Action Class
    actions = ActionChains(driver)
    gender_radio = driver.find_element(By.XPATH, "//label[text()='Male']")
    actions.move_to_element(gender_radio).click().perform()
    print("4. Action Class - passed")

    # Implement Select Class
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    state_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "state")))
    actions.move_to_element(state_dropdown).click().perform()  # Open dropdown
    state_option = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='NCR']")))
    state_option.click()
    print("5. Select Class - passed")

    time.sleep(5)

except TimeoutException as e:
    print(f"Timeout occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
    print("Browser closed.")

