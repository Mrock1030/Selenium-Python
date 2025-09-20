
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage



class LoggedInSuccesfullyPage(BasePage):
    
    __url="https://practicetestautomation.com/practice-test-exceptions/"
    __header_locater= (By.TAG_NAME,'h1')
    __log_out_button_locator= (By.LINK_TEXT,'Log out')
    
    def __init__(self,driver:WebDriver):
        super().__init__(driver)
    
    @property
    def expected_url(self) -> str:
        return self.__url
    
    @property
    def header(self) -> str:
       return super()._get_text(self.__header_locator)
   
    
    def is_logout_button_displayed(self)->bool:
       return super().is_displayed(self.__log_out_button_locator)

        
     