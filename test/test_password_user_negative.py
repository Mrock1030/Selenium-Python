from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
import pytest


class TestNegativeScenarios:
    
        @pytest.mark.login
        @pytest.mark.negative
        
        def test_positive_login(self):
            #open the driver 
            service = Service("/usr/bin/chromedriver")  # Ajusta si es necesario
            driver = webdriver.Chrome(service=service)
            time.sleep(5)
            #go to the page
            driver.get("https://practicetestautomation.com/practice-test-login/")


            #Type username student into Username field
            username_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/div[1]/input")
            username_locator.send_keys("student")

            #Type password Password123 into Password field
            password_locator= driver.find_element(By.XPATH,'/html/body/div/div/section/section/div[1]/div[2]/input')
            password_locator.send_keys("Prueba")

            #Push Submit button
            submit_button_locator = driver.find_element(By.ID,'submit')
            submit_button_locator.click()
            time.sleep(1)
            
            #Verify new page contains expected text ('Congratulations' or 'successfully logged in')
            text_locator= driver.find_element(By.ID,'error')
            #use ".text" for subtract to text of text locator
            actual_text= text_locator.text
            #we put the assert 
            assert actual_text == "Your password is invalid!", "Error message is not expected"

    