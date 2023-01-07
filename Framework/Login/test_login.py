import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from Framework.utils import excel_utils


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(
            executable_path="F:\\SQA\\Batch09\\AutomationBITM09\\Drivers\\geckodriver.exe")

        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

    def test_login_valid(self):

        file = "F:\\SQA\\Batch09\\AutomationBITM09\\Framework\\TestData\\test_data.xlsx"
        sheet = "Sheet1"

        number_of_rows = excel_utils.row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            username = excel_utils.read_data(file, sheet, r, 1)
            password = excel_utils.read_data(file, sheet, r, 2)

            self.driver.find_element(By.NAME, "username").send_keys(username)
            self.driver.find_element(By.NAME, "password").send_keys(password)
            self.driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button").click()

            time.sleep(3)

            expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
            actual_url = self.driver.current_url

            if expected_url != actual_url:
                excel_utils.write_data(file, sheet, r, 4, "Login successful.")
            else:
                excel_utils.write_data(file, sheet, r, 4, "Login Failed.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
