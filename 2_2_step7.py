import time
import os
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    input1 = browser.find_element_by_css_selector('input[name="firstname"]')
    input1.send_keys('input1')
    
    input1 = browser.find_element_by_css_selector('input[name="lastname"]')
    input1.send_keys('input1')
    
    input1 = browser.find_element_by_css_selector('input[name="email"]')
    input1.send_keys('input1')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    
    input1 = browser.find_element_by_css_selector('input[name="file"]')
    input1.send_keys(file_path)
    
    
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()