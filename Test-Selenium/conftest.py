from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():

    print ("Creating chorme driver")
    service = Service("/usr/bin/chromedriver") 
    my_driver = webdriver.Chrome(service=service)
    #add yield if u want return something and keep write code in the same function
    yield my_driver
    print ("Closing chorme driver")
    my_driver.quit()
    