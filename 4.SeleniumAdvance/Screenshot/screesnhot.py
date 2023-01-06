import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Screenshot():
    def capture_screenshot(self):
        driver = webdriver.Firefox(
            executable_path="F:\\SQA\\Batch09\\AutomationBITM09\\Drivers\\chromedriver.exe")
        driver.get("https://www.apple.com/")
        time.sleep(5)

        # Scroll to Specific Element
        watch = driver.find_element(By.CSS_SELECTOR, "[data-unit-id='apple-watch-series-8'] .unit-wrapper > [target]")
        driver.execute_script("arguments[0].scrollIntoView(true);", watch)

        driver.get_screenshot_as_file(
            "E:\\Offline_Batch_09\\Projects\\AutomationBITM09\\4.SeleniumAdvance\\Screenshot\\Apple_watch.png")

        

        driver.close()


test_obj = Screenshot()
test_obj.capture_screenshot()
