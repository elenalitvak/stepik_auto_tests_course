from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import math
import time 

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):  
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    button_book = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until (
       EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    
    button_book.click()
    browser. execute_script("window. scrollBy(0, 800)")
 
    x_element = browser.find_element(By.ID, "input_value")  
    x = x_element.text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)

    button_submit = browser.find_element(By.ID, "solve")
    button_submit.click()
    
finally: 
    time.sleep(12)
    browser.quit()



     