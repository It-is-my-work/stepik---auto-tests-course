from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".btn-primary")
    button.click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    el_x = browser.find_element_by_id("input_value")
    x = int(el_x.text)

    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))

    y = calc(x)

    area = browser.find_element_by_id("answer")
    area.send_keys(y)

    button1 = browser.find_element_by_css_selector(".btn-primary")
    button1.click()


finally:
    time.sleep(10)
    browser.quit()