import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
requests.get(url)
response = requests.get(url).json()
print(requests.get(url))
print(response)
stories = []
for story in response:
    print(story)