import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Headless():
    def headless_demo(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = True

        driver = webdriver.Firefox(
            executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe", options=firefox_options)
        driver.get("https://www.apple.com/")
        time.sleep(5)

        # Scroll to Specific Element
        watch = driver.find_element(By.CSS_SELECTOR, "[data-unit-id='apple-watch-series-8'] .unit-wrapper > [target]")
        driver.execute_script("arguments[0].scrollIntoView(true);", watch)

        driver.get_screenshot_as_file(
            "E:\\Offline_Batch_09\\Projects\\AutomationBITM09\\4.SeleniumAdvance\\Screenshot\\Apple_watch_headless.png")

        driver.close()


test_obj = Headless()
test_obj.headless_demo()
