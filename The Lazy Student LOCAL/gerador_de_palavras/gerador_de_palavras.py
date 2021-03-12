import requests
import random

def gerador_de_palavras():
   japanese_words_link = 'https://raw.githubusercontent.com/Levizera/The-Lazy-Student/master/lists_of_words/japaneseWords.txt'
   english_words_link = 'https://raw.githubusercontent.com/Levizera/The-Lazy-Student/master/lists_of_words/englishWords.txt'
   
   response = requests.get(english_words_link)
   data = response.text
   formatando_arquivo = data.split("\n")
   quantidade_de_palavras = int(input("Quantas palavras você deseja gerar? "))
   
   palavras_aleatorias = random.sample(formatando_arquivo, (quantidade_de_palavras))

gerador_de_palavras()