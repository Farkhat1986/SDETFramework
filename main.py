import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time

# делаем ссылку на сайт для входа
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get('https://demoqa.com/automation-practice-form/')
    time.sleep(2)

    f_name = driver.find_element(By.ID, 'firstName').send_keys('name')

    f_name = driver.find_element(By.ID, 'lastName').send_keys('lastname')


    f_name = driver.find_element(By.ID, 'userEmail').send_keys('fgh@example.com')



    f_name = driver.find_element(By.CSS_SELECTOR, "[for='gender-radio-1']").click()



    f_name = driver.find_element(By.ID, 'userNumber')
    f_name.send_keys('1234567890')


    f_name = driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput').send_keys(Keys.RETURN)

    f_name = driver.find_element(By.ID, 'subjectsInput').send_keys('h')


    f_name = driver.find_element(By.CLASS_NAME, 'subjects-auto-complete__menu').click()

    f_name = driver.find_element(By.CSS_SELECTOR, "[for='hobbies-checkbox-1']").click()

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = driver.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)

    f_name = driver.find_element(By.ID, 'currentAddress')
    f_name.send_keys('ulyanovsk')

    f_name = driver.find_element(By.CSS_SELECTOR, 'div[id="state"]').click()

    f_name = driver.find_element(By.CSS_SELECTOR, f'#react-select-3-option-{random.randint(0, 3)}').click()

    f_name = driver.find_element(By.CSS_SELECTOR, 'div[id="city"]').click()

    f_name = driver.find_element(By.CSS_SELECTOR, 'input[id="react-select-4-input"]').send_keys(Keys.RETURN)

    f_name = driver.find_element(By.CSS_SELECTOR, '#submit').click()

    time.sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

