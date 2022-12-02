from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# options = webdriver.ChromeOptions()
# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s,options=options)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.linkedin.com')
username = driver.find_element(by=By.ID,value="session_key")
password = driver.find_element(by=By.ID,value="session_password")
# username_value = input("Enter your email id : ")
# password_value = input("Enter your password : ")
username.send_keys(os.environ['Linkedin_UID'])
password.send_keys(os.environ['Linkedin_PWD'])
print("Logging IN........")
submit = driver.find_element(by=By.XPATH,value='//*[@id="main-content"]/section[1]/div/div/form/button')
driver.execute_script('arguments[0].click();',submit)
company_names = ['sprinklr','atlassian','phonepe-internet','walmart','google','amazon','microsoft','facebook','meta','netflix','apple']
for i in range(len(company_names)):
    try:
        url = 'https://www.linkedin.com/company/'+company_names[i]+'/people/'
        driver.get(url)
        for i in range(20):
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        all_buttons = driver.find_elements(by=By.TAG_NAME,value="button")
        connect_buttons = [btn for btn in all_buttons if btn.text=='Connect']
        time.sleep(2)
        print("Sent Connection Request to",len(connect_buttons),"people!!")
        for btn in connect_buttons:
            try:
                driver.execute_script('arguments[0].click();',btn)
                time.sleep(1)
                send = driver.find_element_by_xpath('//button[@aria-label="Send now"]')
                driver.execute_script('arguments[0].click();',send)
                time.sleep(1)
            except :
                continue
    except:
        continue
