import csv

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_login_form(driver):
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(5)

    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')
    submit_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    submit_button.click()
    # assert 'Welcome' in driver.page_source
