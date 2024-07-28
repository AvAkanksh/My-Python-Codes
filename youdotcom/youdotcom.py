#!/usr/bin/python
import requests
import json
import urllib.parse
import sys


def main():
    queryString = " ".join(sys.argv[1:])

    params = {
        "q" : queryString
    }
    query = urllib.parse.urlencode(params)
    url = f"https://you.com/api/streamingSearch?{query}&domain=youchat"

    payload = {}
    headers = {
        'User-Agent': 'm',
        'Referer' : 'https://you.com/' 
    }

    req = requests.Session();
    response = req.get( url, headers=headers, data=payload)

    response = response.text
    lines = response.strip().split('\n')
    extracted_text = ""

    for line in lines:
        if line.startswith("data: {\"youChatToken\""):
            data = json.loads(line.split("data: ")[1])
            extracted_text += data["youChatToken"]

    print("-------------")
    print(extracted_text.strip())


if(__name__ == "__main__"):
    main()
