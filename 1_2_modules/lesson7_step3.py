from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_css_selector('#num1')
y_element = browser.find_element_by_css_selector('#num2')
x = x_element.text
y = y_element.text
sum = int(x) + int(y)
value = str(sum)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(value)

button = browser.find_element_by_xpath("//button[@class='btn btn-default']")
button.click()

