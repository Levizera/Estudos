import requests
import json

base_url = 'https://swapi.dev/api'
endpoint_planets = 'planets'
endpoint_people = 'people'

url = base_url + '/' + endpoint_people + '/1'
response = requests.get(url)
content_json = response.json()

print(json.dumps(content_json, indent= 4))