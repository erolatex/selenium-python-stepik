from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")
button = browser.find_element_by_xpath("//button[@class='btn btn-default']")

answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(y)
browser.find_element_by_xpath("//label[contains(text(),'Подтверждаю, что являюсь роботом')]").click();
browser.find_element_by_xpath("//label[contains(text(),'Роботы рулят')]").click()

button.click()

