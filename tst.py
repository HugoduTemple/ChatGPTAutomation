from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_path = r"C:\Users\Owner\Desktop\chromedriver-win64\chromedriver.exe"

options = Options()
options.binary_location = chrome_path
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # Adjust the port if needed

# Ensure Chrome is launched with remote debugging before running this
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://www.google.com")
print(driver.title)

driver.quit()
