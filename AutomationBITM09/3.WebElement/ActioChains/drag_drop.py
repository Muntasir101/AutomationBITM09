import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class DragDrop():
    def element_drag_drop(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")
        driver.get("https://material.angular.io/cdk/drag-drop/examples")
        time.sleep(5)

        source_element = driver.find_element(By.CSS_SELECTOR, "cdk-drag-drop-axis-lock-example .example-box:nth-of-type(2)")
        target_element = driver.find_element(By.CSS_SELECTOR, "cdk-drag-drop-axis-lock-example .example-box:nth-of-type(1)")

        all_action = ActionChains(driver)

        all_action.drag_and_drop(source_element, target_element).perform()
        time.sleep(5)

        driver.close()


test_obj = DragDrop()
test_obj.element_drag_drop()
