from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from datetime import datetime
import pyautogui as py
import json
import cv2
from PIL import ImageGrab


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
time.sleep(20)

# currentPosition = py.position()
# position= (currentPosition[0]*2,currentPosition[1]*2)
# print(position)

print("Logged IN........")

# checking if color is blue  : (  8, 24, 64,255) (NEW UI) {oneWeb}
# checking if color is white : (240,241,242,255) (OLD UI)

image = ImageGrab.grab()
position = (60,1600)
color = image.getpixel(position)
flag = True

if(color[0]==240): 
    print("Old UI")
    time.sleep(0.5)
    py.click(690,425)
    time.sleep(0.5)
    py.click(715,500)
    flag = False

if(color[0]==8):
    print("New UI")
    start = [570,540]
    py.click(start[0],start[1])
    time.sleep(0.5)
    py.click(start[0],start[1]+55)
    print("Selected Option Out of Office")
    time.sleep(0.5)
    py.click(start[0]+180,start[1]-30)
    flag = False

if(flag):
    print("Check if there is any change in the UI")

print("Clicked on Punched In/Out")
time.sleep(10)
