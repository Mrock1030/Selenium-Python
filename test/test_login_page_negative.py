from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
import pytest

@pytest.fixture()
def driver():

    print ("Creating chorme driver")
    service = Service("/usr/bin/chromedriver") 
    my_driver = webdriver.Chrome(service=service)
    #add yield if u want return something and keep write code in the same function
    yield my_driver
    print ("Closing chorme driver")
    my_driver.quit()
    
class TestNegativeScenarios:
    
    @pytest.mark.login
    @pytest.mark.negative
    
    def test_negative_username(self, driver):
        #service = Service("/usr/bin/chromedriver")  # Ajusta si es necesario
        #driver = webdriver.Chrome(service=service)
        
        #open Page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        
        #Type username incorrectUser into Username field
        username_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/div[1]/input")
        username_locator.send_keys("incorrectUser")

        #Type password Password123 into Password field
        password_locator= driver.find_element(By.XPATH,'/html/body/div/div/section/section/div[1]/div[2]/input')
        password_locator.send_keys("Password123")
        time.sleep(1)

        #Push Submit button
        submit_button_locator = driver.find_element(By.ID,'submit')
        submit_button_locator.click()
        time.sleep(1)


        #Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator= driver.find_element(By.ID,'error')
        #use ".text" for subtract to text of text locator
        actual_text= text_locator.text
        #we put the assert 
        assert actual_text == "Your username is invalid!", "Error message is not expected"
        time.sleep(1)
        
        
    @pytest.mark.login
    @pytest.mark.negative     
    def test_negative_password(self, driver):
      
        #service = Service("/usr/bin/chromedriver")  # Ajusta si es necesario
        #driver = webdriver.Chrome(service=service)
        
        #go to the page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(1)

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
            

          
