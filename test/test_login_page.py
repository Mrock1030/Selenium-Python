
from selenium.webdriver.common.by import By
import time 
import pytest
from page_objects.login_page import LoginPage
from page_objects.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException




class TestPositiveScenarios:
    
        @pytest.mark.login
        @pytest.mark.positive
        
        #add driver in function 
        def test_positive_login(self, driver):
            
            login_page = LoginPage(driver)
            
                    
            #Open Page
            login_page.open_url()
            #Push Submit button
            login_page.exucte_login("student","Password123")

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