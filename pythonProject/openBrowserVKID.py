import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

print("test1")
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)
print("test2")
# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке https://suninjuly.github.io/text_input_task.html
driver.get("https://id.vk.com/")
time.sleep(5)
print("test3")
# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать

# Найдем кнопку : ВОЙТИ ЧЕРЕЗ VK ID
submit_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Войти через VK ID')]")

# Нажмём кнопку : ВОЙТИ ЧЕРЕЗ VK ID
submit_button.click()
time.sleep(5)

# Ищем поле для ввода текста
text = driver.find_element(By.CSS_SELECTOR, ".vkuiInput__el")

# Напишем текст в поле
text.send_keys("9811591070")
time.sleep(5)

# Найдем кнопку
continue_button = driver.find_element(By.CSS_SELECTOR, "span.vkuiButton__content")
print("test4")

# Нажать на кнопку
continue_button.click()
time.sleep(100)

print("test final")

# Закрыть окно браузера
# driver.quit()