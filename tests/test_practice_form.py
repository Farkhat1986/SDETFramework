import pytest
from pages.practice_form_page import PracticeFormPage


def test_signup_form(driver):
    practice_form_page = PracticeFormPage(driver)
    practice_form_page.fill_form("First", "Last", "email@example.com", "1234567890", "Jan 1990", "Physics", "Main Street 12")
    practice_form_page.check_form_submission()