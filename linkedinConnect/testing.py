from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.linkedin.com')
username = driver.find_element(by=By.ID,value="session_key")
password = driver.find_element(by=By.ID,value="session_password")
username.send_keys(os.environ['Linkedin_UID'])
password.send_keys(os.environ['Linkedin_PWD'])
print("Logging IN........")
submit = driver.find_element(by=By.XPATH,value='/html/body/main/section[1]/div/div/form/div[2]/button')
driver.execute_script('arguments[0].click();',submit)
company_names = ['sprinklr','atlassian','phonepe-internet','walmart','google','amazon','microsoft','facebook','meta','netflix','apple']
url = 'https://www.linkedin.com/company/'+company_names[0]+'/people/'
driver.get(url)
time.sleep(5)
all_buttons = driver.find_elements(by=By.TAG_NAME,value="button")
connect_buttons = [btn for btn in all_buttons if btn.text=='Connect']
# print(connect_buttons)
# time.sleep(2)
for btn in connect_buttons:
    try:
        # driver.switch_to
        driver.execute_script('arguments[0].click();',btn)
        time.sleep(1)
        # print(driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]'))
        # print(driver.find_elements(by=By.CSS_SELECTOR, value='button span'))
        # button_span = driver.find_elements(by=By.CSS_SELECTOR, value='button span')
        # send = [btn for btn in button_span if btn.text=="Send"
        wait = WebDriverWait(driver, 5);
        send = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Send']")))
        send.click()
    except :
        print("Continueing")
        continue


