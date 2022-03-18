import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")
response = r.json()
print(f"Keys: {response.keys()}")
# print(f"Response: {r.json()}")
print(f"Total Repositories: {response['total_count']}")
repositories = response['items']
print(f"Foundes Repositories: {len(repositories)}")
