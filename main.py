from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 

#open the driver 
service = Service("/usr/bin/chromedriver")  # Ajusta si es necesario
driver = webdriver.Chrome(service=service)
time.sleep(5)


#go to the page
driver.get("https://practicetestautomation.com/practice-test-login/")


#Type username student into Username field
element_labe1 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/div[1]/input")
#Type password Password123 into Password field
element_labe1_2= driver.find_element(By.XPATH,'/html/body/div/div/section/section/div[1]/div[2]/input')

#Push Submit button
element_button= driver.find_element(By.ID,'submit')

#Verify new page URL contains practicetestautomation.com/logged-in-successfully/

#Verify new page contains expected text ('Congratulations' or 'successfully logged in')

#Verify button Log out is displayed on the new page

