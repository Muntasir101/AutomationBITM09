import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Login():
    def login_valid(self):
        driver = webdriver.Firefox(
            executable_path="F:\\SQA\\Batch09\\AutomationBITM09\\Drivers\\geckodriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

        username.send_keys("Admin")
        password.send_keys("admin123")
        login_button.click()

        time.sleep(3)

        expected_text = "Dashboard"
        actual_text = driver.find_element(By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb-module").text

        if expected_text == actual_text:
            print("Login successful.Test Passed")
        else:
            print("Login failed.Test Failed.")

        driver.close()

    def login_invalid(self):
        driver = webdriver.Firefox(
            executable_path="F:\\SQA\\Batch09\\AutomationBITM09\\Drivers\\geckodriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

        username.send_keys("Admin1212")
        password.send_keys("admin1231212")
        login_button.click()

        time.sleep(3)

        expected_error_message = "Invalid credentials"
        actual_error_message = driver.find_element(By.CSS_SELECTOR, ".oxd-alert-content-text").text

        if expected_error_message == actual_error_message:
            print("Test Passed for invalid credentials")
        else:
            print("Test Failed for invalid credentials")

        driver.close()


test_obj = Login()
test_obj.login_valid()
test_obj.login_invalid()
