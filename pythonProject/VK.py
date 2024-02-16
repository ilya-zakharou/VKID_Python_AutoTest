import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Инициализация драйвера браузера
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)  # Установка неявного ожидания для всего драйвера, чтобы избежать жестких time.sleep

try:
    # Шаг 1: Открыть страницу
    driver.get("https://id.vk.com/")

    # Шаг 2: Найти и нажать кнопку "Войти через VK ID"
    submit_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Войти через VK ID')]")
    is_enabled = not submit_button.get_attribute("disabled")
    if is_enabled:
        print("Кнопка 'Продолжить' активна")
    else:
        print("Кнопка 'Продолжить' не активна")
    time.sleep(10)
    submit_button.click()  # Нажать кнопку: "Войти через VK ID"

    # Шаг 3: Найти поле для ввода текста
    text = driver.find_element(By.CSS_SELECTOR, ".vkuiInput__el")  # Найти поле для ввода текста
    text.send_keys("9811591070")  # Ввести текст в поле
    time.sleep(5)
    # Шаг 4: Нажать кнопку "Continue"
    continue_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Continue')]")  # Найти кнопку Продолжить
    find_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    if find_button.get_attribute("disabled") == "true":
        print("Кнопка не активна")
    else:
        print("Кнопка активна")

    time.sleep(5)
    continue_button.click()  # Нажать на кнопку

    # Шаг 5: Дополнительные проверки или действия после нажатия кнопки Продолжить
    # Здесь можно добавить проверки или действия, которые нужно выполнить после нажатия кнопки Продолжить

except Exception as e:
    print("Произошла ошибка на шаге:", e)

finally:
    # Шаг 6: Закрыть окно браузера в любом случае, даже если произошла ошибка
    time.sleep(150)
    driver.quit()