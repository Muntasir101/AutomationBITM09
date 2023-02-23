import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


class Login():
    def login_valid(self):
        # Configure logging
        logging.basicConfig(filename='test.log', level=logging.INFO)

        driver = webdriver.Firefox(
            executable_path="F:\\SQA\\Batch09\\AutomationBITM09\\Drivers\\geckodriver.exe")
        logging.info('Navigating to login page')
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        logging.info('Locating email fields')
        username = driver.find_element(By.NAME, "username")

        logging.info('Locating password fields')
        password = driver.find_element(By.NAME, "password")

        logging.info('Locating Login button')
        login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

        logging.info('Entering Email')
        username.send_keys("Admin")

        logging.info('Entering Password')
        password.send_keys("admin123")

        logging.info('Click to Login button')
        login_button.click()

        time.sleep(3)

        logging.info('Verifying Login')
        expected_text = "Dashboard"
        actual_text = driver.find_element(By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb-module").text

        if expected_text == actual_text:
            print("Login successful.Test Passed")
            logging.info('Login successful.Test Passed')
        else:
            logging.info('Login Unsuccessful.Test Failed.')
            print("Login failed.Test Failed.")

        logging.info('Closing browser window')
        driver.close()


test_obj = Login()
test_obj.login_valid()

