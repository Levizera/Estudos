# Criar uma abstração

class Fila:

# Meio de inserir dados na abstração - Nesse caso um container(lista)
    def __init__(self):    
        self.fila = []

# Metodo para "manipulação" dos objetos/atributos
    def entrar_na_fila(self, nome):
        self.fila.append(nome)

    
    def sair_da_fila(self):
        self.fila.pop(0)





'''
# Criar uma instancia
supermercado = Fila()

# Inserindo e tirando "Valores" de dentro instancia

# Inserindo
supermercado.entrar_na_fila('Levi')
supermercado.entrar_na_fila('Pedro')
supermercado.entrar_na_fila('Lucas')

print(supermercado.fila)


# Retirando
supermercado.sair_da_fila()
supermercado.sair_da_fila()

print(supermercado.fila)
'''
