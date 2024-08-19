from selenium import webdriver
import pytest
from pages.practice_form_page import PracticeFormPage
from selenium.webdriver.chrome.options import Options


class TestPracticeForm:
    @pytest.fixture
    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--headless=new')
        #options.add_argument('--no-sandbox')
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://demoqa.com/automation-practice-form")
        yield driver
        driver.quit()

    def test_signup_form(self, driver):
        practice_form_page = PracticeFormPage(driver)
        practice_form_page.fill_form("First", "Last", "email@example.com", "1234567890", "01 Jan 1990", "Physics", "Main Street 12", "State 1", "City 1")
        practice_form_page.check_form_submission()