from selenium import webdriver
import math
import time

link = 'https://SunInJuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer1 = browser.find_element_by_id("answer")
    answer1.send_keys(y)
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    button.click()
    assert True

finally:
    time.sleep(15)
    browser.quit()
