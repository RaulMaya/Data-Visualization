import requests

from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")
response = r.json()
print(f"Keys: {response.keys()}")
# print(f"Response: {r.json()}")
print(f"Total Repositories: {response['total_count']}")
repositories = response['items']
print(f"Founded Repositories: {len(repositories)}")
# repository = repositories[0]
# repo_names = []
repo_links = []
stared_repos = []
hover_text = []
for repository in repositories:
    # repo_names.append(repository['name'])
    print(repository['name'])
    print(repository['owner']['login'])
    owner = repository['owner']['login']
    stared_repos.append(repository['stargazers_count'])
    print(repository['stargazers_count'])
    print(repository['html_url'])
    print(repository['description'])
    link2repo = f"<a href='{repository['html_url']}'>{repository['name']}</a>"
    repo_links.append(link2repo)
    description = repository['description']
    hover_text.append(f"Owner: {owner}<br />About: {description}")
    print('')

data = [{
    'type':'bar',
    'x':repo_links,
    'y':stared_repos,
    'hovertext':hover_text,
    'marker':{
        'color': 'rgb(215, 240, 150)',
        'line':{'width': 3, 'color' : 'rgb(103, 186, 109)'}
    }
}]

my_layout = {
    'paper_bgcolor':'rgba(0,0,0,0)',
    'plot_bgcolor':'rgba(0,0,0,0)',
    'title':"<a href='https://github.com/RaulMaya/Data-Visualization/blob/master/python_programs/working%20with%20APIs/api_responses.py'>Most Stared Python Projects on GitHub</a>",
    'title_x':0.5,
    'titlefont':{'size':24},
    'xaxis': {'title':'Repository Name',
    'titlefont': {'size':20},
    'tickfont':{'size':12},
    },
    'yaxis': {'title': 'Number of Stars',
    'titlefont': {'size':20},
    'tickfont':{'size':12},
    }}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='python_repos.html')
