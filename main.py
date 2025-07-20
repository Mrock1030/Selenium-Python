from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 

service = Service("/usr/bin/chromedriver")  # Ajusta si es necesario
driver = webdriver.Chrome(service=service)
time.sleep(5)

driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(10)
