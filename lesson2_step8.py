from selenium import webdriver
import os
from time import sleep


url = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(url)

try:
    input1 = browser.find_element_by_css_selector("input[name='firstname']")
    input1.send_keys('done')

    input2 = browser.find_element_by_css_selector("input[name='lastname']")
    input2.send_keys('done')

    input3 = browser.find_element_by_css_selector("input[name='email']")
    input3.send_keys('done')

    file_input = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    file_input.send_keys(file_path)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()
finally:
    sleep(10)
    browser.quit()
