from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://elevate.peoplestrong.com/altLogin.jsf')
username = driver.find_element(by=By.ID,value="loginForm:username12")
password = driver.find_element(by=By.ID,value="loginForm:password")
data = json.load(open("/Users/adugani.vanjari/Documents/GitRepositories/My-Python-Codes/PaytmLogin/credentials.json"))
username.send_keys(data['username'])
password.send_keys(data['password'])
submit = driver.find_element(by=By.XPATH,value='//*[@id="loginForm:loginButton"]/span')
driver.execute_script('arguments[0].click();',submit)
cookies = driver.get_cookies();
for cookie in cookies :
    if(cookie['name']=='SessionToken'):    
        print(cookie['value'].strip('"'))
        break