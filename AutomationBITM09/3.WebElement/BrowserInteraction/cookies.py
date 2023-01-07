import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Cookies():
    def all_cookies(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        cookies = driver.get_cookies()
        for cookie in cookies:
            print(cookie)

        # Add cookie
        driver.add_cookie({
            'name': 'Automation Cookie',
            'value': '1234567Bangladesh',
            'path': '/web',
            'domain': 'opensource-demo.orangehrmlive.com',
            'secure': True,
            'httpOnly': True,
            'sameSite': 'Strict'
        })

        cookies = driver.get_cookies()
        for cookie in cookies:
            print("After add new cookie...............")
            print(cookie)

        driver.delete_all_cookies()
        print("After deleting all cookies...............")

        cookies = driver.get_cookies()
        for cookie in cookies:
            print(cookie)

        driver.close()


test_obj = Cookies()
test_obj.all_cookies()
