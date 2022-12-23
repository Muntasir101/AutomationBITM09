import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElement():
    def locators(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

        username.send_keys("Admin")
        password.send_keys("admin123")
        login_button.click()


test_obj = FindElement()
test_obj.locators()
