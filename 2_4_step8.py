import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element ((By.ID, "price"), "$100")
        )
    
    button = browser.find_element_by_id("book")
    button.click()
    
    x = int(browser.find_element_by_id('input_value').text)
    c = str(math.log(abs(12*math.sin(int(x)))))
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(c)
    
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()