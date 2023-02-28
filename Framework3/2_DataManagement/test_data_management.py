import csv

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def read_test_data():
    test_data = []
    with open('users.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            test_data.append(row)
    return test_data


def test_login_form(driver):
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(5)
    test_data = read_test_data()
    for data in test_data:
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
        username_field.send_keys(data['username'])
        password_field.send_keys(data['password'])
        submit_button.click()
        # assert 'Welcome' in driver.page_source
