from translate import Translator
from time import sleep 

def englishToPortuguese():   
   idiomas = Translator(from_lang="english", to_lang='Portuguese')
   resposta = idiomas.translate(input("Digite a Palavra que deseja traduzir: "))
   
   print("Processando...")
   sleep(2)
   print(resposta.upper())

def japaneseToPortugues():   
   idiomas = Translator(from_lang='japanese', to_lang='Portuguese')
   resposta = idiomas.translate(input("Digite a Palavra que deseja traduzir: "))
   
   print("Processando...")
   sleep(2)
   print(resposta.upper())

def germanToPortugues():   
   idiomas = Translator(from_lang='german', to_lang='Portuguese')
   resposta = idiomas.translate(input("Digite a Palavra que deseja traduzir: "))
   print("Processando...")
   sleep(2)
   print(resposta.upper())
   
selecaoDeIdioma = int(input(''' 
Selecione o idioma em que está o seu texto

[1] Inglês
[2] Japonês
[3] Alemão
'''))

if selecaoDeIdioma == 1:
   print(englishToPortuguese())
elif selecaoDeIdioma == 2:
   print(japaneseToPortugues())
elif selecaoDeIdioma == 3:
   print(germanToPortugues())
else:
   print('Opcão Inválida, Tente novamente!!!')
   exit()