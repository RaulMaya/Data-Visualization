from asyncore import read
from urllib import request
import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
requests.get(url)
response = requests.get(url).json()
print(requests.get(url))
print(response)
# Creating file to store json
readable_file = 'hacker_news_file.json'
with open(readable_file, 'w') as f:
    json.dump(response, f, indent=4)