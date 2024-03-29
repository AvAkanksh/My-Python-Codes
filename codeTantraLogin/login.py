from selenium import webdriver
import time

browsers = ['brave', 'firefox']
browser = browsers[0]
# browser = browsers[int(input('Choose a browser: \n1)Brave\n2)Firefox\nEnter you choice (1 or 2)\n:'))-1]

if(browser == "brave"):
    driver_path = "/usr/local/share/chromedriver"
    brave_path = "/usr/bin/brave"
    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    option.add_argument('--disable-notification')
    # option.add_argument("--incognito") #OPTIONAL
    # option.add_argument("--headless") #OPTIONAL
    driver = webdriver.Chrome(executable_path=driver_path, options=option)

if(browser == "firefox"):
    driver_path = '/usr/local/share/geckodriver'
    firefox_path = "/usr/bin/firefox"
    option = webdriver.FirefoxOptions()
    option.binary_location = firefox_path
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    option.add_argument('--disable-notification')
    # option.add_argument("--incognito") #OPTIONAL
    # option.add_argument("--headless") #OPTIONAL
    driver = webdriver.Firefox(executable_path=driver_path, options=option)

driver.get("https://iittp.codetantra.com/login.jsp")

username = driver.find_element_by_id("loginId")
username.clear()
username.send_keys("abc@gmail.com")

password = driver.find_element_by_name("password")
password.clear()
password.send_keys("xxxxxxxxxxx")

driver.find_element_by_id("loginBtn").click()
time.sleep(0.1)
driver.find_element_by_link_text("Tests").click()
