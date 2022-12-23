from selenium import webdriver

class Firefox():
    def firefox_config(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")

        driver.get("https://google.com")


test_obj = Firefox()
test_obj.firefox_config()