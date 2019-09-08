import time
import math
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    
    browser.implicitly_wait(5)
    
    browser.get(link)
    
    browser.find_element_by_id("button")

finally:
    time.sleep(5)
    browser.quit()