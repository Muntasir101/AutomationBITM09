from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time


class FirefoxDriverManager():
    def config_firefox(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://google.com")
        time.sleep(5)


test_firefox = FirefoxDriverManager()
test_firefox.config_firefox()
