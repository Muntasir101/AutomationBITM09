import time
from selenium import webdriver
import unittest
from Framework2.page.login_page import LoginPage
from Framework2.page.myinfo import MyInfoPage


class LoginTest(unittest.TestCase):

    def test_login(self):
        driver = webdriver.Firefox(
            executable_path="F:\\SQA\\Batch09\\AutomationBITM09\\Drivers\\geckodriver.exe")

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        obj = LoginPage(driver)
        obj.login_orange("Admin", "admin123")

        obj = MyInfoPage(driver)
        obj.update_info()

        time.sleep(3)

        driver.close()
