
from selenium.webdriver.common.by import By
import time 
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class TestExceptions:
    
    @pytest.mark.exceptions
    def test_no_such_element_exeception(self,driver):
        
        #open search
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        

        #Click Add button
        botton_add = driver.find_element(By.XPATH,"/html/body/div/div/section/section/div/div[1]/div/button[3]")
        botton_add.click()
        
        wait = WebDriverWait(driver, 20)
        row_2_input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        #Verify Row 2 input field is displayed
        #row_2_input_locator = driver.find_element(By.XPATH, '(//input[@class="input-field"])[2]')
        #show is row is display
        assert row_2_input_locator.is_displayed(),"Row 2 input should be displayed, but it's not"
    
    
    def test_element_not_interactable_exeception(self,driver):
        #open search
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        

        #Click Add button
        botton_add = driver.find_element(By.XPATH,"/html/body/div/div/section/section/div/div[1]/div/button[3]")
        botton_add.click()
        
        wait = WebDriverWait(driver, 20)
        row_2_input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        

        #Verify Row 2 input field is displayed
        #show is row is display
        assert row_2_input_locator.is_displayed(),"Row 2 input should be displayed, but it's not"
        row_2_input_locator.click()
        
        # Type text into the second input field
        row_2_input_locator.send_keys("Hot dog")
        
        #Push Save button using locator By.name(“Save”)
        save_button = WebDriverWait(driver, 15).until(
        ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/section/section/div/div[3]/div/button[1]')))
        save_button.click()

        message_save = driver.find_element(By.ID, "confirmation")
        
        #Verify text saved
        confirmation_message_save =  message_save.text
        assert message_save.is_displayed(),"Row 2 was saved, but it's not"
        
    def test_stale_element_reference_exception(self,driver):
        
        #open search
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        
 
        #Verify text saved
        
        intructions_element = driver.find_element(By.ID, "instructions")
        intructions_element =  intructions_element.text
        
        #Push add button
        push_button_add = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/button[3]").click()
        
        #Find the instructions text element
        wait= WebDriverWait(driver, 20)
        assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions"))),"instruction text element should be displayed"
             
    def test_time_out_exception(self,driver):
        #open search
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        

        #Click Add button
        push_button_add = driver.find_element(By.XPATH, "/html/body/div/div/section/section/div/div[1]/div/button[3]").click()
   
        #Wait for 3 seconds for the second input field to be displayed
        wait= WebDriverWait(driver, 3)
        second_label= wait.until(ec.invisibility_of_element_located((By.XPATH, "/html/body/div/div/section/section/div/div[3]/div/input")),"Failed waiting for Row 2 input to be visible")
        
        # Verify second input field is displayed
        assert second_label,"instruction text element should be displayed"

           
   
        
        
        
        
        
        
        
        
    
        
        
        