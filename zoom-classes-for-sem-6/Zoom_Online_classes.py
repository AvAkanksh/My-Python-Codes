from datetime import date
import keyboard
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def alert_accept():
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()

Principle_Of_Measurement = ['https://zoom.us/j/96849277139?pwd=L0lHcHloT3Q0ZTd2UFh6WVlJUC9PQT09',
                            'https://zoom.us/j/98575905413?pwd=OHQ0Y2RFTkFaNmpjZ3V0a0V5cTB2Zz09',
                            'https://zoom.us/j/93658580649?pwd=elRpd0g0anBSK3dkVExZbldRRllkUT09']
International_Trade_and_Finance = ['https://zoom.us/j/92145706546?pwd=dWI5dGpRUEs0RzhITjlIY1puclB0QT09',
                                   'https://zoom.us/j/91861529678?pwd=U3h4dEpJUm1rTnJxa1RER0F2MDVMZz09',
                                   'https://meet.google.com/lookup/e5tj53eliq?authuser=1&hs=179']

Machine_Learning_For_Image_Processing = 'https://zoom.us/j/97384784172?pwd=MFJQcGxwL1IzQVRZaXQzTEUwbnFiUT09'
Analog_Circuts_Lab = 'https://zoom.us/j/97826638010?pwd=REtHclhVYVBDNXB1THgvSDAwU0lndz09'
Computer_Vision = 'https://zoom.us/j/9094160862?pwd=UEJ5N29QNWtHNkZDd3ZUU1JsSnhyZz09'
Power_Systems = 'https://zoom.us/j/94328850879?pwd=ZjdmaVBTWVJNRVlEdDRzMDl1NHJsQT09'
weekdayNumber = date.today().weekday()
# -----------------------------------------------------------------------
# Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday
# -----------------------------------------------------------------------
#   0         1          2          3         4         5          6
# -----------------------------------------------------------------------
currentTime = int(time.strftime("%H%M", time.localtime()))
done = 0
t1 = time.time()
runtime = time.time()-t1
while (((done) != 1) and (runtime < 5)):
    if (weekdayNumber == 0):
        if (900 <= currentTime <= 950):
            url = Power_Systems
            done = 1
        elif (1000 <= currentTime <= 1050):
            url = Computer_Vision
            done = 1
        elif (1100 <= currentTime <= 1150):
            url = Machine_Learning_For_Image_Processing
            done = 1
        elif (1400 <= currentTime <= 1450):
            url = International_Trade_and_Finance[0]
            done = 1
    elif (weekdayNumber == 1):
        if (900 <= currentTime <= 950):
            url = Principle_Of_Measurement[0]
            done = 1
        elif (1100 <= currentTime <= 1150):
            url = Power_Systems
            done = 1
        elif (1200 <= currentTime <= 1250):
            url = Power_Systems
            done = 1
        elif (1500 <= currentTime <= 1550):
            url = Analog_Circuts_Lab
            done = 1
    elif (weekdayNumber == 2):
        if (900 <= currentTime <= 950):
            url = Computer_Vision
            done = 1
        elif (1000 <= currentTime <= 1050):
            url = Machine_Learning_For_Image_Processing
            done = 1
        elif (1100 <= currentTime <= 1150):
            url = Principle_Of_Measurement[1]
            done = 1
        elif (1200 <= currentTime <= 1250):
            url = Principle_Of_Measurement[1]
            done = 1
    elif (weekdayNumber == 3):
        if (1000 <= currentTime <= 1050):
            url = Power_Systems
            done = 1
        elif (1100 <= currentTime <= 1150):
            url = Computer_Vision
            done = 1
        elif (1400 <= currentTime <= 1450):
            url = International_Trade_and_Finance[1]
            done = 1
    elif (weekdayNumber == 4):
        if (900 <= currentTime <= 950):
            url = Machine_Learning_For_Image_Processing
            done = 1
        elif (1000 <= currentTime <= 1050):
            url = Principle_Of_Measurement[2]
            done = 1
        elif (1200 <= currentTime <= 1250):
            url = International_Trade_and_Finance[2]
            done = 1
    runtime = time.time() - t1
try:
    driver.get(url)
    time.sleep(0.1)
    alert_accept()
    print('\n' * 20,  '-'*100, '\n\tOpened the link in :',
          time.time() - t1, 'seconds.\n'), '-'*100
    time.sleep(1)
    driver.close()
except Exception:
    print('\n'*20, '-'*100, '\n\tCouldn\'t open the link ! Total time wasted :',
          time.time()-t1, 'seconds.\n', '-'*100)
    driver.close()
