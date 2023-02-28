"""
Litres
"""
from selenium.webdriver.common.by import By
import time

def test_litres(browser):
    """
    Authorization
    Выполняет авторизацию на сайте
    """
    browser.get("https://www.litres.ru/")
    
    email = browser.find_element(By.CSS_SELECTOR, value="a.Login-module__loginLink_2wpb4")
    email.click()
    login = browser.find_element(By.CSS_SELECTOR, value="button.ButtonV1-module__button_32fds")
    login.click()
    emailfiled = browser.find_element(By.CSS_SELECTOR, value=".AuthorizationPopup-module__input_2KwTn")
    emailfiled.click()
    emailfiled.send_keys("") # вставить логин
    auth_button = browser.find_element(By.CSS_SELECTOR, value=".ButtonV1-module__button_32fds.AuthorizationPopup-module__button_2rBsl.ButtonV1-module__button__primary_3xeqb.ButtonV1-module__button__orange_2zBoI")
    auth_button.click()
    time.sleep(2)
    password_filed = browser.find_element(By.CSS_SELECTOR, value=".AuthorizationPopup-module__input_2KwTn")
    password_filed.send_keys("") # вставить пароль
    time.sleep(2)
    auth_button1 = browser.find_element(By.CSS_SELECTOR, value=".ButtonV1-module__button_32fds")
    auth_button1.click()
    time.sleep(100)

    
    assert True, ""
    
"""
Author today
"""
from selenium.webdriver.common.by import By
import time

def test_smoke3(browser):
    """
    Authorization
    Выполняет авторизацию на сайте и переход в библиотеку пользователя
    """
    browser.get("https://author.today//")
    
    entrance = browser.find_element(By.CSS_SELECTOR, value="#navbar-right > li:nth-child(2) > a")
    entrance.click()
    time.sleep(5)
    login = browser.find_element(By.ID, value="Login")
    password = browser.find_element(By.CSS_SELECTOR, value="#authModal > div > div > div.modal-body > div > div > div > form:nth-child(2) > div:nth-child(4) > input")
    login.send_keys("") # вставить логин
    password.send_keys("") # вставить пароль
    entrance2 = browser.find_element(By.CSS_SELECTOR, value="#authModal .btn.btn-primary.btn-block.mt-lg")
    entrance2.click()
    time.sleep(10)
    library = browser.find_element(By.CSS_SELECTOR, value="#navbar > ul > li:nth-child(4) > a")
    library.click()
    time.sleep(10)

    assert True, ""