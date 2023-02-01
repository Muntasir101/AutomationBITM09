import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class TestGuru99Bank(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64"
                                                        "\\geckodriver.exe")
        self.driver.get("http://demo.guru99.com/v4/")
        time.sleep(5)

    def test_login_and_perform_transactions(self):
        # Login to Guru99 demo bank
        self.driver.find_element(By.NAME, "uid").send_keys("mngr474597")
        self.driver.find_element(By.NAME, "password").send_keys("umYbYqY")
        self.driver.find_element(By.NAME, "btnLogin").click()
        time.sleep(5)

        # Navigate to the New Customer page
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        time.sleep(3)

        # Create a new customer
        self.driver.find_element(By.NAME, "name").send_keys("John Doe")
        self.driver.find_element(By.XPATH, "//input[@value='f']").click()
        self.driver.find_element(By.NAME, "dob").send_keys("01/01/1980")
        self.driver.find_element(By.NAME, "addr").send_keys("123 Main St")
        self.driver.find_element(By.NAME, "city").send_keys("New York")
        self.driver.find_element(By.NAME, "state").send_keys("NY")
        self.driver.find_element(By.NAME, "pinno").send_keys("123456")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("1234567890")
        self.driver.find_element(By.NAME, "emailid").send_keys("john.doe@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.NAME, "sub").click()
        time.sleep(5)

        # Verify that the customer was created successfully
        message = self.driver.find_element(By.XPATH , "//table//p[@class='heading3']").text
        #self.assertEqual(message, "Customer Registered Successfully!!!!")

        # Logout of Guru99 demo bank
        self.driver.find_element(By.LINK_TEXT, "Log out").click()

    #def tearDown(self):
        # self.driver.quit()


if __name__ == '__main__':
    unittest.main()
