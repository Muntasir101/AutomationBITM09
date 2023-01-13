import time

from selenium.webdriver.common.by import By


class MyInfoPage():
    def __init__(self, driver):
        self.driver = driver

    def update_info(self):
        print("My info updated succesfully.")


