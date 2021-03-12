import requests
import json

url = 'https://swapi.dev/api/planets/1/'
response = requests.get(url)
status_code = response.status_code
content_json = response.json()

#Formatando Json 
#print(json.dumps(content_json, indent= 4))

#Imprimindo Valores especificos do Json 
name = content_json['name']
terrain = content_json['terrain']
climate = content_json['climate']
population = content_json['population']

print(f''' 
Nome do Local: {name}
Estado do terreno: {terrain}
Clima: {climate}
Tamanho da População: {population}
''')