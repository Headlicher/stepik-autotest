from selenium import webdriver
import os
import time

link = 'http://suninjuly.github.io/file_input.html'
curent_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(curent_dir, 'hello.txt')

try:
    str = "Pizda"
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_elements_by_class_name("form-control")
    for element in first_name:
        element.send_keys(str)
    upload = browser.find_element_by_id("file")
    upload.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(15)
    browser.quit()
