import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import allure

class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, email, mobile, dob, subjects, address, state, city):
        with allure.step('fill name'):
            self.driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys(first_name)
        with allure.step('fill last name'):
            self.driver.find_element(By.XPATH, "//*[@id='lastName']").send_keys(last_name)
        with allure.step('fill email'):
            self.driver.find_element(By.ID, "userEmail").send_keys(email)
        with allure.step('fill gender'):
            self.driver.find_element(By.CSS_SELECTOR, "[for='gender-radio-1']").click()
        with allure.step('fill mobile number'):
            self.driver.find_element(By.CSS_SELECTOR, "#userNumber").send_keys(mobile)
        with allure.step('fill date birth'):
            self.driver.find_element(By.CSS_SELECTOR, "#dateOfBirthInput").send_keys(dob)
        with allure.step('fill subjects'):
            self.driver.find_element(By.ID, 'subjectsInput').send_keys('h')
        with allure.step('fill subjects complete menu'):
            self.driver.find_element(By.CLASS_NAME, 'subjects-auto-complete__menu').click()
        with allure.step('fill hobbies'):
            self.driver.find_element(By.CSS_SELECTOR, "[for='hobbies-checkbox-1']").click()
        with allure.step('scroll window'):
            self.driver.execute_script("window.scrollBy(0, 300);")

            # self.driver.find_element(By.CSS_SELECTOR, "#uploadPicture").send_keys("file.txt")
            #current_dir = os.path.abspath(os.path.dirname(__file__))
            #file_name = "file.txt"
            #file_path = os.path.join(current_dir, file_name)
            #self.driver.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)

        with allure.step('fill address'):
            self.driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys(address)
        with allure.step('fill state'):
            self.driver.find_element(By.CSS_SELECTOR, 'div[id="state"]').click()
        with allure.step('fill state choice'):
            self.driver.find_element(By.CSS_SELECTOR, f'#react-select-3-option-{random.randint(0, 3)}').click()
        with allure.step('fill sity'):
            self.driver.find_element(By.CSS_SELECTOR, 'div[id="city"]').click()
        with allure.step('fill sity choice'):
            self.driver.find_element(By.CSS_SELECTOR, 'input[id="react-select-4-input"]').send_keys(Keys.RETURN)
        with allure.step('click button'):
            self.driver.find_element(By.CSS_SELECTOR, "#submit").click()

    def check_form_submission(self):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "example-modal-sizes-title-lg"), "Thanks for submitting the form"))
        time.sleep(5)