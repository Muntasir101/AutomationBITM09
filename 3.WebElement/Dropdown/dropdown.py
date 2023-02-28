"""
Verify all dropdown options are available
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = driver.find_element(By.CSS_SELECTOR, "select#dropdown")
dropdown_options = Select(dropdown)

# Expected options list
expected_options_list = ['Please select an option', 'Option 1', 'Option 2']

# Create an empty list to store the options
actual_options_list = []

print('Options are: ')
# iterate over dropdown options
for opt in dropdown_options.options:
    option_text = opt.text
    actual_options_list.append(option_text)
    # get option text
    print(opt.text)

print(actual_options_list)

# Compare the expected and actual dropdown lists
assert actual_options_list == expected_options_list, f"Expected options: {expected_options_list}. " \
                                                     f"Actual options: {actual_options_list} "
print("Dropdown options matched.Test Passed")


# browser quit
driver.quit()
