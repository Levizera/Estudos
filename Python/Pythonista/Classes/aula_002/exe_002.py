# Metodos de Fato
# Exercicio da Pizza

class Pizza:
    # Abstração "Geral" da coisa
    # Variaveis da classe são como formas
    # Nesse caso a forma da pizza "Normal" tem 8 pedaços, mas futuramente eu posso criar um metodo que modifique esta forma
    pedacos = 8

    def __init__(self, sabor):
        self.sabor = sabor
        
    def pegar_pedaco(self):
        self.pedacos -= 1
        
    # Mudando valores da própria classe/"Forma"
    @classmethod
    def quantidade_de_pedacos(cls, quantidade):
        cls.pedacos = quantidade
        
    # Static method, é um metodo que não interage com a classe. É como se fosse uma função isolada dentro da classe.
    @staticmethod
    def ingredientes():
        return 'massa, molho de tomate e queijo'
    # -> print(Pizza.ingredientes())    
    