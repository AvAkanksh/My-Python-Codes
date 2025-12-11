from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

import time
import os

# options = webdriver.ChromeOptions()
# s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.linkedin.com/login')
username = driver.find_element(by=By.ID,value="username")
password = driver.find_element(by=By.ID,value="password")
# username = driver.find_element(by=By.ID,value="session_key")
# password = driver.find_element(by=By.ID,value="session_password")
# username_value = input("Enter your email id : ")
# password_value = input("Enter your password : ")
username.send_keys(os.environ['Linkedin_UID'])
password.send_keys(os.environ['Linkedin_PWD'])
print("Logging IN........")
# submit = driver.find_element(by=By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
# submit = driver.find_element(by=By.XPATH,value='/html/body/main/section[1]/div/div/form/div[2]/button')
submit = driver.find_element(by=By.XPATH,value='/html/body/div/main/div[2]/div[1]/form/div[4]/button')
driver.execute_script('arguments[0].click();',submit)
company_names=["gleanwork","maverick-derivatives","cohesity","rubrik-inc","flow-traders","capital-group","da-vinci-trading","nk-securities","quantbox-research-pte","quadeye","micron-technology","worldquant","gravitonresearchcapital","millennium-partners","blackstonegroup","gulftalent.com","sprinklr","alpha-grep","edge-focus","eversana","quicksell","eightfoldai-eightfold","abacusai","klacorp","trepup","infurnia","trilogyinnovations","rippling","mediatek","invygo-app","sharechat","enphase-energy","lekconsulting","amazon","slbglobal","fast-retailing","morgan-stanley","vmock-inc","teachmint","morgan-stanley","zetasuite","vamstar","skiify","accenture-japan","jpmorganchase",'atlassian','phonepe-internet','walmart','google','amazon','microsoft','facebook','meta','netflix','apple']
#company_names = ['sprinklr','atlassian','phonepe-internet','walmart','google','amazon','microsoft','facebook','meta','netflix','apple']
#company_names=["nk-securities"]
random.shuffle(company_names)
wait = WebDriverWait(driver, 4)
print("--"*40)
for company in company_names:
    try:
        url = 'https://www.linkedin.com/company/'+company+'/people/'
        driver.get(url)
        # time.sleep(5)
        for k in range(20):
            time.sleep(0.5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 1000);")
            try :
                send = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Show more results']")))
                send.click()
            except:
                continue

        all_buttons = driver.find_elements(by=By.TAG_NAME,value="button")
        connect_buttons = [btn for btn in all_buttons if btn.text=='Connect']
        time.sleep(0.8)
        requestCounter = 0
        requestCounterNegative = 0
        # print("Sent Connection Request to",len(connect_buttons),"people!!")
        for btn in connect_buttons:
            try:
                driver.execute_script('arguments[0].click();',btn)
                time.sleep(0.1)
                try:
                    send = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Send without a note']")))
                    send.click()
                    # time.sleep(0.5)
                    send = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Send']")))
                    send.click()
                except:
                    pass
                time.sleep(0.1)

                requestCounter= requestCounter+1
            except :
                requestCounterNegative= requestCounterNegative+1
        print(company,":",requestCounter,"/",(requestCounterNegative+requestCounter)," connection requests sent successfully!")
        print("--"*40)
        # print("Sent ",count,"requests from",company_names[i])
    except:
        print('Didnt find any connect buttons')
