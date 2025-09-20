from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):
    __url="https://practicetestautomation.com/practice-test-exceptions/"
    __username_field =(By.XPATH, "/html/body/div/div/section/section/div[1]/div[1]/input")
    __password_field= (By.XPATH,'/html/body/div/div/section/section/div[1]/div[2]/input')
    __submit_button=  (By.ID,'submit')
   
    def __init__(self,driver:WebDriver):
        super().__init__= driver
    
    def open(self):
        super().open_url(self.__url)
    
    def execute_login(self,__username_field:str ,__password_field:str):
        
        super()._type(self.__username_field,username)
        super()._type(self.__password_field, password)
        super()._type(self.__submit_button)
