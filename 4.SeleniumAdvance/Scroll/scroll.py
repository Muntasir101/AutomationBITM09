import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Scroll():
    def webpage_scroll(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")
        driver.get("https://www.apple.com/")
        time.sleep(5)

        # Scroll Down
        driver.execute_script('scrollBy(0, 5000);')
        time.sleep(3)

        # Scroll Up
        driver.execute_script('scrollBy(0, -5000);')

        # Scroll to Specific Element
        watch = driver.find_element(By.CSS_SELECTOR, "[data-unit-id='apple-watch-series-8'] .unit-wrapper > [target]")
        driver.execute_script("arguments[0].scrollIntoView(true);", watch)

        # driver.close()


test_obj = Scroll()
test_obj.webpage_scroll()
