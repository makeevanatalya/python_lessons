# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    from selenium.webdriver.chrome.service import Service
    s = Service("C:\\drivers\\chromedriver.exe")
    browser = webdriver.Chrome(service=s)
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока не появится 100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element(By.XPATH, ".//button[@id='book']")
    button.click()

    x_element=browser.find_element(By.XPATH, "//span[@id='input_value']")
    x=x_element.text
    y=calc(x)
    input1 = browser.find_element(By.XPATH, "//input[@class='form-control']")
    input1.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()
    time.sleep(10)

finally:
# закрываем браузер после всех манипуляций
    browser.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
