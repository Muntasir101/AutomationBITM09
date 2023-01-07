import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Navigation():
    def navigating(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

        username_enable = username.is_enabled()
        username_display = username.is_displayed()

        password_enable = password.is_enabled()
        password_display = password.is_displayed()

        if username_enable == True and username_display == True:
            username.send_keys("Admin")
        else:
            print("Bug Found !!! Username is not enabled or disabled.")

        if password_enable == True and username_display == True:
            password.send_keys("admin123")
        else:
            print("Bug Found !!! Password is not enabled or disabled.")

        login_button.click()
        time.sleep(3)

        driver.back()
        time.sleep(3)

        driver.forward()
        time.sleep(2)

        expected_text = "Dashboard"
        actual_text = driver.find_element(By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb-module").text

        if expected_text == actual_text:
            print("Test Passed")
        else:
            print("Test Failed.")

        driver.close()


test_obj = Navigation()
test_obj.navigating()
