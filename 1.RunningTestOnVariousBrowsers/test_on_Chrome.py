from selenium import webdriver

class Launch_Chrome():
    def chrome_config(self):
        driver = webdriver.Chrome(executable_path="E:\\Offline_Batch_09\\Tools\\chromedriver_win32\\chromedriver.exe")

        driver.get("https://google.com")


test_obj = Launch_Chrome()
test_obj.chrome_config()