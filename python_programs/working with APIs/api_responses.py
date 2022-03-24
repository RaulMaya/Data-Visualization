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
repo_names = []
stared_repos = []
for repository in repositories:
    repo_names.append(repository['name'])
    print(repository['name'])
    print(repository['owner']['login'])
    stared_repos.append(repository['stargazers_count'])
    print(repository['stargazers_count'])
    print(repository['html_url'])
    print(repository['description'])
    print('')

data = [{
    'type':'bar',
    'x':repo_names,
    'y':stared_repos,
    'marker':{
        'color': 'rgb(255, 159, 69)',
        'line':{'width': 3, 'color' : 'rgb(247, 110, 17)'}
    }
}]

my_layout = {
    'title':'Most Stared Python Projects on GitHub',
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
