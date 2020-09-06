from selenium import webdriver
import time

link = 'http://suninjuly.github.io/wait1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.implicitly_wait(5)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    verify = browser.find_element_by_id("verify_message")
    assert "successful" in verify.text

finally:
    time.sleep(15)
    browser.quit()
