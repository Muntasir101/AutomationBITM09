import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import pytest
from Framework2.page.login_page import LoginPage
from Framework2.utils import excel_utils

class LoginTest(unittest.TestCase):

    def test_login(self):
        driver = webdriver.Firefox(
            executable_path="F:\\SQA\\Batch09\\AutomationBITM09\\Drivers\\geckodriver.exe")

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        file = "F:\\SQA\\Batch09\\AutomationBITM09\\Framework2\\data\\test_data2.xlsx"
        sheet = "Sheet1"

        number_of_rows = excel_utils.row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            username_data = excel_utils.read_data(file, sheet, r, 1)
            password_data = excel_utils.read_data(file, sheet, r, 2)

            obj = LoginPage(driver)
            obj.login_orange(username_data, password_data)

            time.sleep(3)

            expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
            actual_url = driver.current_url

            if expected_url != actual_url:
                excel_utils.write_data(file, sheet, r, 4, "Login successful.")
            else:
                excel_utils.write_data(file, sheet, r, 4, "Login Failed.")

        driver.close()





