from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    __url="https://practicetestautomation.com/practice-test-exceptions/"
    __username_field =(By.XPATH, "/html/body/div/div/section/section/div[1]/div[1]/input")
    __password_field= (By.XPATH,'/html/body/div/div/section/section/div[1]/div[2]/input')
    __submit_button=  (By.ID,'submit')
   
    def __init__(self,driver:WebDriver):
        self._driver= driver
    
    def open(self):
        self._driver.get(self.__url)
    
    def execute_login(self,__username_fiel:str ,__password_field:str):
        
        wait =WebDriverWait(self._driver,10)
        wait.until(ec.invisibility_of_element_located(self.__username_field))
        self._driver.find_element(self.__username_field).send_keys(username)
        wait.until(ec.invisibility_of_element_located(self.__password_field))
        self._driver.find_element(self.__password_field).send_keys(password)
        wait.until(ec.invisibility_of_element_located(self.__submit_button))
        self._driver.find_element(self.__submit_button).click()
        

        

    