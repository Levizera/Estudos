import re

#Encontrando coisas com Regular Expressions
arq = open('japanese_words.txt', 'r')
'''
#Procurando linhas que contenham a palavra 'person'
for line in arq:
    line = line.rstrip()
    if re.search('person', line):
        print(line)
'''
'''
#Para procurar arquivos que ocaracter seja o selecionado, se usa o "^"
for line in arq:
    line = line.rstrip()
    if re.search('^じ', line):
        print(line)
'''
#Extraindo dados com Regular Expressions

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)

#Procurando palavras ou letras

palavras = 'Eu Estava la Quando Algo terrivel aconteceu'
procurar = re.findall('[AEIOU]', palavras)
print(procurar)
