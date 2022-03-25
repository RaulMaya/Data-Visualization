import requests
from operator import itemgetter
import json

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
requests.get(url)
response = requests.get(url).json()
stories = []
for story in response:
    url = f'https://hacker-news.firebaseio.com/v0/item/{story}.json'
    individual_story = requests.get(url).json()
    print(individual_story)
    story_dict = {
        'title': individual_story['title'],
        'author': individual_story['by'],
        'score': individual_story['score'],
        'comments': individual_story['descendants'],
        'url': individual_story['url']
    }
    stories.append(story_dict)

stories = sorted(stories, key=itemgetter('comments'), reverse=True)

for story in stories:
    print(story)