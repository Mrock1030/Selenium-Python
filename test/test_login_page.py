from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
import pytest


#add the new function about driver, if u want to repeat call driver in test
@pytest.fixture()
def driver():

    print ("Creating chorme driver")
    service = Service("/usr/bin/chromedriver") 
    my_driver = webdriver.Chrome(service=service)
    #add yield if u want return something and keep write code in the same function
    yield my_driver
    print ("Closing chorme driver")
    my_driver.quit()
    

class TestPositiveScenarios:
    
        @pytest.mark.login
        @pytest.mark.positive
        
        #add driver in function 
        def test_positive_login(self, driver):
                    
            #go to the page
            driver.get("https://practicetestautomation.com/practice-test-login/")
            time.sleep(1)

            #Type username student into Username field
            username_locator = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div[1]/div[1]/input")
            username_locator.send_keys("student")

            #Type password Password123 into Password field
            password_locator= driver.find_element(By.XPATH,'/html/body/div/div/section/section/div[1]/div[2]/input')
            password_locator.send_keys("Password123")

            #Push Submit button
            submit_button_locator = driver.find_element(By.ID,'submit')
            submit_button_locator.click()
            time.sleep(1)

            #Verify new page URL contains practicetestautomation.com/logged-in-successfully/
            #para verficar el nuevo url de la pagina
            actual_url = driver.current_url
            #we put the assert 
            assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"


            #Verify new page contains expected text ('Congratulations' or 'successfully logged in')
            text_locator= driver.find_element(By.TAG_NAME,'h1')
            #use ".text" for subtract to text of text locator
            actual_text= text_locator.text
            #we put the assert 
            assert actual_text == "Logged In Successfully","Error message is not expected"

            #Verify button Log out is displayed on the new page
            log_out_button_locator= driver.find_element(By.LINK_TEXT,'Log out')
            #we put the assert 
            assert log_out_button_locator.is_displayed()
            time.sleep(1)