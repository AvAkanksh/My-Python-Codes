import requests
from bs4 import BeautifulSoup

url = "https://cdma.cgg.gov.in/CDMA_PT/ViewAssessments/CitizenAsmtSearch"

payload = {'I_ASMT_NO': '1211402715',
'CaptchaText': '5Ramo1'}
files=[

]
headers = {
  'Connection': 'keep-alive',
  'Cookie': 'ASP.NET_SessionId=egdnlwrpxqljpjxdlos0jsj4'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

soup = BeautifulSoup(response.text)

soup = 

print(soup)