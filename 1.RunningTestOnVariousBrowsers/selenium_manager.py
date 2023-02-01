# Need Selenium4.6.0 to implement selenium_manager
# Don't need to give driver path
from selenium import webdriver
import time
from selenium.webdriver.common.selenium_manager import SeleniumManager

driver = webdriver.Firefox()
time.sleep(5)
driver.get("https://google.com")

driver.close()
