
import requests

hero_list = ['Hulk', 'Captain America', 'Thanos']
hero_dict = {}

url = "https://akabab.github.io/superhero-api/api"
uri = "/all.json"
res = requests.get(url + uri)
json = res.json()
for i in json:
    if i['name'] in hero_list:
        hero_dict[i['powerstats']['intelligence']] = i['name']
print(hero_dict[max(hero_dict)])
