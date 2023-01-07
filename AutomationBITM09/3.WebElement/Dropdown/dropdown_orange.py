import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Dropdown():
    def select_dropdown(self):
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

        time.sleep(3)

        admin = driver.find_element(By.LINK_TEXT, "Admin")
        admin.click()
        time.sleep(2)

        add_admin_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-header-container .oxd-button--secondary")
        add_admin_button.click()

        user_role = driver.find_element(By.CSS_SELECTOR, "//div[@class='oxd-select-text-input'])[1]")

        if user_role is not None:
            print("User Role Dropdown found.")
        else:
            print("User Role Dropdown Not Found")


test_obj = Dropdown()
test_obj.select_dropdown()
