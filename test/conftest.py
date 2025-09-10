from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture()
def driver(request):
    #found the browser|
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver ")
    
    if browser == "chrome":
        service = Service("/usr/bin/chromedriver") 
        my_driver = webdriver.Chrome(service=service)
          
    elif browser == "firefox":
        my_driver= webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError (f"Expected chrome  or firefox, but got {browser} ")
    
    #add yield if u want return something and keep write code in the same function
    #my_driver.implicitly_wait(10)
    yield my_driver
    print (f"Closing {browser} driver") 
    
    my_driver.quit()
    
def pytest_addoption(parser):
    parser.addoption(
    "--browser", action="store", default="chrome", help="browser to excute test(chrome or firefox)")
        
