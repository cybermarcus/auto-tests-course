from selenium import webdriver
from time import sleep
from lesson3_step4 import calc


browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(url)

try:
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()
finally:
    sleep(10)
    browser.quit()
