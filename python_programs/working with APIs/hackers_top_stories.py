import requests
from operator import itemgetter
import json
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
requests.get(url)
response = requests.get(url).json()
stories = []
for story in response:
    url = f'https://hacker-news.firebaseio.com/v0/item/{story}.json'
    individual_story = requests.get(url).json()
    try:
        story_dict = {
            'title': individual_story['title'],
            'author': individual_story['by'],
            'score': individual_story['score'],
            'comments': individual_story['descendants'],
            'url': individual_story['url']
        }
        stories.append(story_dict)
    except:
        pass

stories = sorted(stories, key=itemgetter('comments'), reverse=True)

titles = []
authors = []
scores = []
comments = []
urls = []

for story in stories:
    titles.append(f"<a href='{story['url']}'>{story['title']}</a>")
    authors.append(story['author'])
    scores.append(story['score'])
    comments.append(story['comments'])

data = [{
    'type':'bar',
    'x':titles[:15],
    'y':comments[:15],
    'hovertext':authors[:15],
    'marker':{
        'color': 'rgb(198, 155, 123)',
        'line':{'width': 3, 'color' : 'rgb(247, 204, 172)'}
    }
}]

my_layout = {
    'title':'Hacker News',
    'title_x':0.5,
    'titlefont':{'size':24},
    'xaxis': {'title':'News Title',
    'titlefont': {'size':20},
    'tickfont':{'size':12},
    },
    'yaxis': {'title': 'Number of Comments',
    'titlefont': {'size':20},
    'tickfont':{'size':12},
    }}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='hacker-news.html')
