from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from datetime import datetime
import pyautogui as py
options = webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s,options=options)
driver.maximize_window()
driver.get('https://elevate.peoplestrong.com/altLogin.jsf')
username = driver.find_element(by=By.ID,value="loginForm:username12")
password = driver.find_element(by=By.ID,value="loginForm:password")
username.send_keys(os.environ['Paytm_Username'])
password.send_keys(os.environ['Paytm_Password'])
print("Logging IN........")
submit = driver.find_element(by=By.XPATH,value='//*[@id="loginForm:loginButton"]/span')
driver.execute_script('arguments[0].click();',submit)
time.sleep(23)
print("Logged IN........")
py.click(695,425)
py.click(700,485)
print("Selected Option Out of Office")
# Set the location of the punch out according to your screen!
py.click(900,390)
print("Clicked on Punched In/Out")
time.sleep(7)