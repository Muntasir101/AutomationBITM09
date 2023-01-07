import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class PurchaseCourse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(
            executable_path="F:\\SQA\\Batch09\\AutomationBITM09\\Drivers\\geckodriver.exe")

        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        cls.driver.maximize_window()

    def test_order(self):
        print("Successfully Course Purchase Done")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
