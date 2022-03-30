from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x1,x2):
  return str(int(x1)+int(x2))
try: 
    link = " http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x1_element = browser.find_element_by_id("num1")
    x1 = x1_element.text
    x2_element = browser.find_element_by_id("num2")
    x2 = x2_element.text
    y = calc(x1,x2)
    # Ваш код, который заполняет обязательные поля
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(y) # ищем элемент

     

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

   

   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()