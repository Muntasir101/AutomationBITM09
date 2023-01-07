import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class Register(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(
            executable_path="F:\\SQA\\Batch09\\AutomationBITM09\\Drivers\\geckodriver.exe")

        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        cls.driver.maximize_window()

    def test_register(self):
        print("Successfully registered")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
