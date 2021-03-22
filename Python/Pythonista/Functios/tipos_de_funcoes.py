'''
Os 3 tipos de Funções
1 - Funções nomeadas (def)
2 - Funções anonimas (lambda)
3 - Funções de classe (class)
'''

# Função Nomeada
def nomeada_soma(x, y):
    return x + y


#Função Anônima
anonima_soma = lambda x, y: x + y


#Função de Classe
class classe_soma:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        return self.x + self.y


