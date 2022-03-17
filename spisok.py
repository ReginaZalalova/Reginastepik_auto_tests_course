from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    one = browser.find_element(By.XPATH,'//span[@id="num1"]')
    x = one.text
    two = browser.find_element(By.XPATH, '//span[@id="num2"]')
    y = two.text
    def sum(x,y):
        return str(int(x)+int(y))
    v = sum(x,y)
    select = Select(browser.find_element(By.XPATH,'//select[@class="custom-select"]'))
    select.select_by_value(v)
    button = browser.find_element(By.XPATH,'//button[@type="submit"]')
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла