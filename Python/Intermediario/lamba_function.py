# --> forma de executar: print(somar_10(4, 3))

somar_10 = lambda x: x + y


# --> Colocando inputs dentro da função "lambda"
# --> print(somar(x, y))

# x = int(input('Insira um numero: '))
# y = int(input('Insira mais um numero: '))
somar = lambda x, y: x * y

# --> Organizando listas com lambda

my_list = [(1, 2), (6, 5), (8, 5), (4, 0)]
organizando = sorted(my_list, key = lambda x: x[1])
org_pela_soma = sorted(my_list, key = lambda x: x[0] + x[1])