import requests
import random

def gerador():
   target_url = "https://raw.githubusercontent.com/Levizera/The-Lazy-Student/master/Word-Generator/japaneseWords.txt"
   
   response = requests.get(target_url)
   data = response.text
   spliting = data.split("\n")
   how_much = int(input("Quantas palavras você deseja gerar? "))
   a = random.sample(spliting, (how_much))
   print(a)
   
gerador() 