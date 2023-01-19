from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from datetime import datetime

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
print(submit)
time.sleep(5)
out_of_office=driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div/app-root/div/div[1]/div/div/div/div/div/app-home/app-card/div/div/div[2]/app-punch-inout/div/div[1]/div/div/a[2]')
driver.execute_script('arguments[0].click();',out_of_office)
punch_in = driver.find_element(by=By.CLASS_NAME,value="punch-in")
punch_out = driver.find_element(by=By.CLASS_NAME,value="punch-out")
hrs=int(datetime.now().strftime("%H"))
if(hrs<12):
    driver.execute_script('arguments[0].click();',punch_in)

else:
    driver.execute_script('arguments[0].click();',punch_out)
time.sleep(2)
