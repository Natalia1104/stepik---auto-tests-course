from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    val = browser.find_element_by_id("input_value")
    val_text = val.text
    y = calc(val_text)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()
    
    
    
    radio_button = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()
        
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()