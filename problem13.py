import requests

url_list = [
    
]

for url in url_list:
    requests.get(url)


result = requests.get('https://github.com/timeline.json')

print(result.json())
