'''
--> O que é um set?? <--
--> Os sets são uma coleção de itens desordenada, imutável e que não podem conter elementos duplicados. Por ser parcialmente imutável, os sets possuem permissão de adição e remoção de elementos.
'''


# --> Set básico
set_classico = {'levi', 1, True, 32, 'ferreira', 7,  False, 23}


# --> Set que divide as letras de uma string
dividindo_letras = set('Levi')


# --> Set vazio
set_vazio = set()


# --> Adicionando valores ao set
# --> Somente um valor pode ser adicionado por vez nome_do_set.add(valor)
adicionando_valores = set()

# --> adicionando_valores.add(1)
# --> adicionando_valores.add('levi')
# --> adicionando_valores.add('ferreira')


# --> Removendo valores
# --> removendo_valores.remove('levi')
removendo_valores = {'levi', 1, 'ferreira', 2}


# --> Discartando elemtentos de dentro do set
# --> discartando_elementos.discard('levi')
discartando_elementos = {'levi', 'ferreira', 'da', 'silva'}


# --> Limpando um set 
# --> limpando_elementos.clear()
limpando_elementos = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


# --> Tirando elemento do set e mostrando ele 
# --> mostrando_elemento.pop()
mostrando_elemento = {'levi', 'ferreira', 'silva'}


# --> Juntando 2 sets
# --> unindo = impar.union(par)

impar = {1, 3, 5, 7, 9}
par = {2, 4, 6, 8}
unindo = impar.union(par)


# --> Vendo os valores iguais de dois sets
# --> valores1.intersection(valores2)
valores1 = {1, 2, 3, 4, 5, 6, 7, 'levi'}
valores2 = {2, 3, 4, 'levi'}
intersecting = valores1.intersection(valores2)


# --> Vendo a diferença entre os sets
# --> É mostrado os valores do primeiro set que não estão no segundo
# --> valores1.intersection(valores2)
setA = {1,2,3,4,5}
setB = {1,2,3,7,8}
diff = setA.difference(setB)