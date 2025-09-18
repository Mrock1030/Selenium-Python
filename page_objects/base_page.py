

class BasePage:
    
    def __init__(self, driver,WebDriver):
        self._driver = driver
        
    def _find(self, locator:tuple)-> WebElement:
        self._driver.find_element(*locator)
        
    def _type(self,locator:tuple, text:str):
        self._find(locator).send_keys(text)
    
    def wait_until_element_is_visible(self,locator:tuple, time:int=10):
        wait =WebDriverWait(self._driver, time)
        wait.until(ec.invisibility_of_element_located(locator))
    
    def _click(self, locator:tuple, time: int=10):
        self._wait_until_element_is_visible(locator,time)
        self._find(locator).click()
        
    @property
    def current_url(self)-> str:
        return self._driver.current_url
    
    def is_displayed(self,locator:tuple)->bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False 
        
        
    
        