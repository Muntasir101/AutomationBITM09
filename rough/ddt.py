from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# load data from a CSV file into a pandas DataFrame
data = pd.read_csv("E:\\Offline_Batch_09\\Projects\\AutomationBITM09\\Framework\\TestData\\test_data.csv")

# initialize a webdriver instance
driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_09\\Tools\\geckodriver-v0.32.0-win64\\geckodriver.exe")

# loop through each row in the data
for index, row in data.iterrows():
    # navigate to the website
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    # find and interact with the form elements
    # wait for an element to be present on the page
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button"))
    )

    # enter the values from the current row of data
    username_field.send_keys(row["Username"])
    password_field.send_keys(row["Password"])

    # submit the form
    submit_button.click()

    # assert the expected outcome
    #assert "Welcome, " + row["Username"] in driver.page_source

# close the webdriver instance
driver.quit()
