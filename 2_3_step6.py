import time
import math
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    
    # time.sleep(3)
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x = int(browser.find_element_by_id('input_value').text)
    c = str(math.log(abs(12*math.sin(int(x)))))
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(c)
    
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()