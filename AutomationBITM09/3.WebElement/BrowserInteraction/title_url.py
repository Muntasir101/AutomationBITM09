import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TitleUrl():
    def title_url(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        title = driver.title
        print(title)

        url = driver.current_url
        print(url)

        driver.close()


test_obj = TitleUrl()
test_obj.title_url()
