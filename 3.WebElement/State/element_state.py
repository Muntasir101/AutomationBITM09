import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementState():
    def check_state(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

        username_enable = username.is_enabled()
        print(username_enable)

        username_display = username.is_displayed()
        print(username_display)

        if username_enable == True and username_display == True:
            username.send_keys("Admin")
        else:
            print("Bug Found !!! Element is not enabled or disabled.")

        driver.close()


test_obj = ElementState()
test_obj.check_state()
