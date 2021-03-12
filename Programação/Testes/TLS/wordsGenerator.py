from random import choice
import random
	
def geradorDePalavrasJap():
	arquivo = open('japaneseWords.txt', 'r')
	lerArquivo = arquivo.readlines()
	quantidadeDePalavras = int(input('Quantas palavras deseja Gerar? '))
	geradorAleatorio = random.sample(lerArquivo, (quantidadeDePalavras))
	print(geradorAleatorio)
	
def geradorDePalavrasEng():
	arquivo = open('englishWords.txt', 'r')
	lerArquivo = arquivo.readlines()
	quantidadeDePalavras = int(input('Quantas palavras deseja Gerar? '))
	geradorAleatorio = random.sample(lerArquivo, (quantidadeDePalavras))
	print(geradorAleatorio)   
   
selecionarIdioma = int(input(''' 

======================================
Escolha um idioma para estudar agora

[1] Inglês
[2] Japonês

======================================

Selecione uma opção: 
'''))
   
if selecionarIdioma == 1:
   print(geradorDePalavrasEng())
elif selecionarIdioma == 2:
   print(geradorDePalavrasJap())
else:
   print('Comando não reconhecido, Releia as opções acima e tente novamente!!')