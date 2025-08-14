
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import pytest



class TestCases:
    
    @pytest.mark.addcar
    @pytest.mark.positive
    
    def test_case_1(self, driver):
        
        driver.maximize_window()  
        driver.get("https://www.floristeriamundoflor.com/")
        time.sleep(3)
        
        #founding categotry love
        category_love= driver.find_element(By.LINK_TEXT, "Amor")
        category_love.click()
        time.sleep(1)
        
        #verify current url
        actual_url =driver.current_url
        assert actual_url=="https://www.floristeriamundoflor.com/product-category/amor/"
        
        #add one product of category love
        image_first_product= driver.find_element(By.CSS_SELECTOR,".image-no-effect.unveil-image")
        
        # Create acction over image product
        action = ActionChains(driver)
        action.move_to_element( image_first_product).perform()
        
        add_first_product = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".title-cart")))
        add_first_product.click()
        time.sleep(5)
        
        #verify current url 
        actual_url = driver.current_url
        assert actual_url == "https://www.floristeriamundoflor.com/carrito/"
        time.sleep(2)
        
        #come back to category love 
        
        wait = WebDriverWait(driver, 10)
        category_love= wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Amor")))    
        category_love.click()
        
        #add second  product of category love
        image_second_product= driver.find_element(By.CSS_SELECTOR,".image-no-effect .unveil-image")
        
        # Create acction over image product
        action = ActionChains(driver)
        action.move_to_element( image_second_product).perform()
        
        add_second_product = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".title-cart")))
        add_first_product.click()
        time.sleep(5)
        
        #verify current url
        actual_url =driver.current_url
        assert actual_url=="https://www.floristeriamundoflor.com/carrito/"
        
        #end to script
        print("Finalizo Correctamente")
        
           
        
        
        
        
        
        

