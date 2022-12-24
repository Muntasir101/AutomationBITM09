import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class MouseHover():
    def open_sub_menu(self):
        driver = webdriver.Firefox(
            executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")
        driver.get("https://demo.opencart.com/")
        time.sleep(5)

        Desktops = driver.find_element(By.LINK_TEXT, "Desktops")

        all_action = ActionChains(driver)

        all_action.move_to_element(Desktops).perform()
        time.sleep(2)

        mac = driver.find_element(By.LINK_TEXT, "Mac (1)")
        mac.click()
        time.sleep(3)

        driver.close()


test_obj = MouseHover()
test_obj.open_sub_menu()
