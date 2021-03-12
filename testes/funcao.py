import random
import requests

japones = 'https://raw.githubusercontent.com/Levizera/The-Lazy-Student/master/lists_of_words/japaneseWords.txt'
ingles = 'https://raw.githubusercontent.com/Levizera/The-Lazy-Student/master/lists_of_words/englishWords.txt'

def teste(x):
   response = requests.get(x)
   data = response.text
   formatando_arquivo = data.split("\n")
   quantidade_de_palavras = int(input("Quantas palavras você deseja gerar? "))
   palavras_aleatorias = random.sample(formatando_arquivo, (quantidade_de_palavras))
   print(palavras_aleatorias)

teste(x)