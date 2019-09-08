import time
import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    c = calc(int(x))
    
    input1 = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(c)
    
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    
    button.click()

finally:
    time.sleep(30)
    browser.quit()