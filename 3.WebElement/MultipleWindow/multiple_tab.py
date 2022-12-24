import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class MultipleWindow():
    def switch_window(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")
        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(5)

        parent_window = driver.current_window_handle

        driver.find_element(By.LINK_TEXT, "Click Here").click()

        all_window = driver.window_handles
        print(all_window)

        for child_window in all_window:
            if child_window not in parent_window:
                driver.switch_to.window(child_window)
                driver.get("https://google.com")
                time.sleep(3)
                #driver.close()

        for child_window in all_window:
            if child_window not in parent_window:
                driver.switch_to.window(parent_window)
                driver.get("https://apple.com")
                time.sleep(3)


test_obj = MultipleWindow()
test_obj.switch_window()
