from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    el = browser.find_element_by_css_selector('button[type="submit"]')
    el.click()
    confirm = browser.switch_to.alert
    confirm.accept()





    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

   

   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()