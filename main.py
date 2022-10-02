import lxml
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup
import time

url = 'https://vk.com/'

'''  ===Создание HTML документа===   '''
def get_html(url):
    driver = webdriver.Chrome(executable_path='chromedriver')

    try:
        driver.get(url=url)
        time.sleep(5)
        
        with open('vksuite.html','w') as file:
            file.write(driver.page_source)

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

'''  ===Заполнение полей Логин/Пароль===   '''
def login(url, username, password):
    driver = webdriver.Chrome(executable_path='chromedriver')

    driver.get(url)
    email_field = driver.find_element(By.XPATH,"//input[@name='login']")
    email_field.send_keys(username)
    time.sleep(1)
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//form/button"))).click()

    login_button = driver.find_element(By.XPATH,"//form/button/span/span")
    login_button.click()
    time.sleep(2)


    password_field = driver.find_element(By.XPATH,"//input[@name='password']")
    password_field.send_keys(password)
    time.sleep(2)

    login_button = driver.find_element(By.XPATH,"//button/span/span/span")
    login_button.click()

    # login_button = self.driver.find_elements_by_class_name("FlatButton__content")
    # login_button.click()

    #
    # login_button = self.driver.find_element_by_class("vkuiButton__content")
    # login_button.click()
    driver.quit()
    # try:
    #
    #
    # except Exception as _ex:
    #     print(_ex)
    # finally:
    #     driver.close()
    #     driver.quit()
def main():
    login(url,username=,password=)

if __name__ == '__main__':
    main()