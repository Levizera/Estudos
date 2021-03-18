from collections import Counter

# --> Contando a quantidade de vezes que um caracter é repetido numa string
# --> Mostrando items em forma de dicionário
# --> print(my_counter)

a = "aaaabbbcccccdddd"
my_counter = Counter(a)
print(my_counter)


# --> Mostrando items em forma de tuples dentro de uma lista
# --> print(my_counter.items())

contando = "aaaabbbcccccdddd"
my_counter = Counter(contando)
print(my_counter.items())


# --> Mostrando os caracteres que foram repetidos 
# --> print(my_counter.keys())

cada_caractere = "aaaabbbcccccdddd"
my_counter = Counter(cada_caractere)
print(my_counter.keys())


# --> Mostrando somente a quantidade de vezes que os caracteres foram repetidos
# --> print(my_counter.values())

valores = "aaaabbbcccccdddd"
my_counter = Counter(valores)
print(my_counter.values())


# --> Mostrando o elemento mais comum da string
# Ele vai mostrar basicamente o elemtento que 'mais se repete'
# --> print(my_counter.most_common(1)) 

mais_comuns = "aaaabbbcccccdddd"
my_counter = Counter(mais_comuns)
print(my_counter.most_common(1))