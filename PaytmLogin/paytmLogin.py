from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from datetime import datetime
import pyautogui as py
import json

options = webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s,options=options)
driver.maximize_window()
driver.get('https://elevate.peoplestrong.com/altLogin.jsf')
username = driver.find_element(by=By.ID,value="loginForm:username12")
password = driver.find_element(by=By.ID,value="loginForm:password")
data = json.load(open("/Users/adugani.vanjari/Documents/GitRepositories/My-Python-Codes/PaytmLogin/credentials.json"))
username.send_keys(data['username'])
password.send_keys(data['password'])
print("Logging IN........")
submit = driver.find_element(by=By.XPATH,value='//*[@id="loginForm:loginButton"]/span')
driver.execute_script('arguments[0].click();',submit)
time.sleep(40)
print("Logged IN........")
py.click(590,370)
time.sleep(0.5)
py.click(600,425)
print("Selected Option Out of Office")
# Set the location of the punch out according to your screen!
time.sleep(0.5)
py.click(770,325)
print("Clicked on Punched In/Out")
time.sleep(15)
