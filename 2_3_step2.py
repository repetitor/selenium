import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.execute_script("prompt('Robots at work');")
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()


time.sleep(30)
browser.quit()