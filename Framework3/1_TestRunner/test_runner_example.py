from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_search_box(driver):
    driver.get('https://www.google.com/')
    driver.implicitly_wait(5)
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('Selenium')
    search_box.submit()
    assert 'Selenium' in driver.title
