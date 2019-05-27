from selenium import webdriver
import time
browser = webdriver.Chrome('.\chromedriver.exe')
browser.get('http://localhost:8000')
assert 'Django' in browser.title
