from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Инициализация драйвера
driver = webdriver.Chrome()
driver.maximize_window()

try:
    #Открытие сайта 
    driver.get("https://avtovokzal-on-line.ru/")
    
    #Ожидание загрузки страницы
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".logo > a > .img-responsive")))

    #Пункт отправления
    WebDriverWait(driver, 15).until(
        lambda d: d.find_element(By.ID, "dispatch-station-id").is_enabled())
        
    from_input = driver.find_element(By.ID, "app-btn-dispatch") 
    from_input.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#select-dispatch-station-modal .modal-body"))) 

    #Нахождение элемента вне области видимости
    dispatch = driver.find_element(By.CSS_SELECTOR, "p:nth-child(84) > .app-change-dispatch-station")
    driver.execute_script("arguments[0].scrollIntoView(true);", dispatch) #Иркутск автовокзал
    time.sleep(1)  # небольшая задержка для стабилизации
    dispatch.click()

    close_dispatch  = driver.find_element(By.CSS_SELECTOR, "#select-dispatch-station-modal span") 
    close_dispatch .click() 

    time.sleep(3)

    #Пункт назначения
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#select-arrival-station-modal .modal-body"))) 

    arrival = driver.find_element(By.CSS_SELECTOR, "p:nth-child(35) > .app-change-arrival-station") #Братск автостанция
    arrival.click()

    time.sleep(3)

    #Дата отправления
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dispatch-date"))) 

    date = driver.find_element(By.ID, "dispatch-date")
    date.send_keys("05.04.2025")

    time.sleep(3)

    #Поиск билетов 
    search_input = driver.find_element(By.CSS_SELECTOR, ".my > .btn")
    search_input.click()

    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ticket-search-schedule"))) 

    if len(results) > 0:
        print(u"\u041d\u0430\u0439\u0434\u0435\u043d\u043e\u0020\u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432\u003a" + str(len(results))) #Найдено результатов:

    else: 
        print(u"\u041d\u0435\u0020\u043d\u0430\u0439\u0434\u0435\u043d\u043e\u0020\u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432") #Не найдено результатов

    time.sleep(3)

except Exception as e: 
    print(f"Error {str(e)}")


finally:
    # Закрытие браузера
    driver.quit()
