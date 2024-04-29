from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from time import sleep

keys_search = ["Selenium", "Python", "OpenAI"]

driver = webdriver.Chrome()
driver.get("http://www.google.com")


for key in keys_search:
    element = driver.find_element(By.NAME, "q")
    element.clear()
    element.send_keys(key)
    element.send_keys(Keys.RETURN)

    sleep(2)
    
'driver.quit()'






