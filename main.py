from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrom_browser = webdriver.Chrome()
chrom_browser.maximize_window()
chrom_browser.get('https://demoqa.com/automation-practice-form')
time.sleep(10)

