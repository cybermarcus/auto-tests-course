from selenium import webdriver
from time import sleep
from math import sin
from math import log as ln


def calc(x):
    return str(ln(abs(12*sin(x))))

def main():
    browser = webdriver.Chrome()
    url = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(url)

    try:
        button = browser.find_element_by_css_selector("button[type='submit']")
        button.click()

        confirm = browser.switch_to.alert
        confirm.accept()
        sleep(2)

        x = browser.find_element_by_id('input_value').text
        y = calc(int(x))

        input = browser.find_element_by_id('answer')
        input.send_keys(y)

        button = browser.find_element_by_css_selector("button[type='submit']")
        button.click()
    finally:
        sleep(10)
        browser.quit()

if __name__ == "__main__":
    main()
