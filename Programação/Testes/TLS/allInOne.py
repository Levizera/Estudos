from random import choice
import random
from translate import Translator
from time import sleep

#Gerador
def geradorJap():
   arquivo = open('japaneseWords.txt', 'r')
   read = arquivo.readlines()
   quantidadeDePalavras = int(input('Quantas palavras deseja gerar? '))
   escolhaRandom = random.sample(read, quantidadeDePalavras)
   print(escolhaRandom)
   
geradorJap()