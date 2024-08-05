import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get('https://demoqa.com/automation-practice-form/') # делаем ссылку на сайт для входа
    time.sleep(2)

    FIRST_NAME = driver.find_element(By.ID, 'firstName').send_keys('name')

    LAST_NAME = driver.find_element(By.ID, 'lastName').send_keys('lastname')

    USER_NAME = driver.find_element(By.ID, 'userEmail').send_keys('fgh@example.com')

    GENDER = driver.find_element(By.CSS_SELECTOR, "[for='gender-radio-1']").click()

    USER_NAMBER = driver.find_element(By.ID, 'userNumber').send_keys('1234567890')

    BIRTH_INPUT = driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput').send_keys(Keys.RETURN)

    SUBJECTS_INPUT = driver.find_element(By.ID, 'subjectsInput').send_keys('h')



    SUBJECTS = driver.find_element(By.CLASS_NAME, 'subjects-auto-complete__menu').click()

    HOBBIES = driver.find_element(By.CSS_SELECTOR, "[for='hobbies-checkbox-1']").click()

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = driver.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)

    CURRENT_ADDRES = driver.find_element(By.ID, 'currentAddress').send_keys('ulyanovsk')

    driver.execute_script("window.scrollBy(0, 300);") # скроллим страницу для выполнения следующих действий

    STATE = driver.find_element(By.CSS_SELECTOR, 'div[id="state"]').click()

    STATE_OPTION = driver.find_element(By.CSS_SELECTOR, f'#react-select-3-option-{random.randint(0, 3)}').click()

    CITY = driver.find_element(By.CSS_SELECTOR, 'div[id="city"]').click()

    CITY_INPUT = driver.find_element(By.CSS_SELECTOR, 'input[id="react-select-4-input"]').send_keys(Keys.RETURN)

    BUTTON = driver.find_element(By.CSS_SELECTOR, '#submit').click()

    time.sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

