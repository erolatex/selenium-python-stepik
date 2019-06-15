from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
input1.send_keys("Ivan")
input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
input3.send_keys("test@test.test")

# Отправляем заполненную форму
button = button = browser.find_element_by_xpath("//button[contains(text(),'Отправить')]")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text


