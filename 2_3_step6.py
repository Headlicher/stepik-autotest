from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    go = browser.find_element_by_class_name("trollface")
    go.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id("input_value")
    x = calc(x_element.text)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(x)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(30)
    browser.quit()
