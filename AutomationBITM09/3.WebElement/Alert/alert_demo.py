import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Alerts():
    def all_alert(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(5)

        normal_alert = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(1) > button")
        normal_alert.click()

        alert_text = driver.switch_to.alert.text
        print(alert_text)

        driver.switch_to.alert.accept()

        confirm_alert = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(2) > button")
        confirm_alert.click()

        driver.switch_to.alert.dismiss()

        prompt_alert = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(3) > button")
        prompt_alert.click()
        time.sleep(2)

        driver.switch_to.alert.send_keys("Test message")
        time.sleep(3)
        driver.switch_to.alert.accept()

        driver.close()


test_obj = Alerts()
test_obj.all_alert()
