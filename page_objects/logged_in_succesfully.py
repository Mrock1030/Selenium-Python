
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage



class LoggedInSuccesfullyPage():
    
    __url="https://practicetestautomation.com/practice-test-exceptions/"
    __header_locater= (By.TAG_NAME,'h1')
    __log_out_button= (By.LINK_TEXT,'Log out')
    
    def __init__(self,driver:WebDriver):
        self._driver= driver
        
    @property
    def current_url(self)-> str:
        return self._driver.current_url
    
    @property
    def expected_url(self) -> str:
        return self.__url
    
    def header(self) -> str:
       return self._driver.find_element(self.__header_locater).text
    
    def is_logout_button_displayed(self)->bool:
       return self._driver.find_element(self.__log_out_button).is_displayed()
        
     