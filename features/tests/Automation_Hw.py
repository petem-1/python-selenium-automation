from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from features.steps.product_search import click_search_icon

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
driver.find_element(By.XPATH,"//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']") .click()
sleep(3)
driver.find_element(By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy']") .click()
sleep(3)
driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']")
actual_results= driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
expected_results='Sign into your Target account'
assert expected_results in actual_results, f'I expected {actual_results} but i got {expected_results}'

print ("Test Passed")

driver.quit()
