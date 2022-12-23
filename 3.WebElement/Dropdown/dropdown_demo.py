import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class dropdown():
    def dropdown_select(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")
        driver.get("https://the-internet.herokuapp.com/dropdown")
        time.sleep(5)

        dropdown = driver.find_element(By.CSS_SELECTOR, "select#dropdown")

        dropdown_options = Select(dropdown)
        dropdown_options.select_by_value("1")


test_obj = dropdown()
test_obj.dropdown_select()