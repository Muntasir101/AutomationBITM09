import unittest
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

global driver

class LoginTest(unittest.TestCase):
    driver = webdriver.Firefox(
        executable_path="F:\\SQA\\Batch09\\AutomationBITM09\\Drivers\\geckodriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)


def test_login_valid(self):
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