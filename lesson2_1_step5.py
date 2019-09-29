from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element_by_id("treasure")
    x = element.get_attribute("valuex")
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()
    
    radio_button = browser.find_element_by_id("robotsRule")
    radio_button.click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()