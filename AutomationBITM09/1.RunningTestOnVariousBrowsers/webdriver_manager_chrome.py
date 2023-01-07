from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time


class ChromeManager():
    def config_chrome(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://google.com")
        time.sleep(5)


test_chrome = ChromeManager()
test_chrome.config_chrome()
