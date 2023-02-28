import time
import configparser
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

"""
logging not working
"""


@pytest.fixture
def driver():

    # Read the configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Get the WebDriver settings from the configuration file
    browser = config.get('WebDriver', 'browser')
    timeout = config.getint('WebDriver', 'timeout')

    # Set up the WebDriver
    if browser == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.implicitly_wait(timeout)

    # Get the website URL from the configuration file
    url = config.get('Website', 'url')
    driver.get(url)

    yield driver
    driver.quit()


def test_login_valid(driver):
    # Load the website
    logging.info("Loading website")

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
