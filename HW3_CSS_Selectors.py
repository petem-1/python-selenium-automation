from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# get the path to the ChromeDriver executable
driver.find_element(By.CSS_SELECTOR,"[class='a-icon a-icon-logo']")
driver.find_element(By.CSS_SELECTOR,"[id='ap_customer_name']")
driver.find_element(By.CSS_SELECTOR,"[id='ap_email']")
driver.find_element(By.CSS_SELECTOR,"[id='ap_password']")
driver.find_element(By.CSS_SELECTOR,"[id='ap_password_check']")
driver.find_element(By.CSS_SELECTOR,"[id='continue']")
driver.find_element(By.CSS_SELECTOR,"[href*='notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR,"[href*='notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR,"[class='a-link-emphasis']")
