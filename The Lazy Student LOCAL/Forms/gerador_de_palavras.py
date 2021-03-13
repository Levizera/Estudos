import requests
import random


japanese_words_link = 'https://raw.githubusercontent.com/Levizera/The-Lazy-Student/master/lists_of_words/japaneseWords.txt'
english_words_link = 'https://raw.githubusercontent.com/Levizera/The-Lazy-Student/master/lists_of_words/englishWords.txt'
french_words_link = 'https://raw.githubusercontent.com/Levizera/The-Lazy-Student/master/lists_of_words/francais.txt'

def gerador_de_palavras(idioma):
    # Processando os links
    response = requests.get(idioma)
    data = response.text
    formatando_arquivo = data.split("\n")
    
    # Input e Output
    quantidade_de_palavras = int(input("Quantas palavras você deseja gerar? "))
    palavras_aleatorias = random.sample(formatando_arquivo, (quantidade_de_palavras))
    print(palavras_aleatorias)

qual_idioma = int(input(''' 
Qual idioma deseja estudar?

[ 1 ] Inglês
[ 2 ] Japonês
[ 3 ] Francês

---> '''))

if qual_idioma == 1:
    gerador_de_palavras(english_words_link)
elif qual_idioma == 2:
    gerador_de_palavras(japanese_words_link)
elif qual_idioma ==3:
    gerador_de_palavras(french_words_link)
else:
    print('Opção Inválida, Tente novamente')
