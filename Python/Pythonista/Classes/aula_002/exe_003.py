# --> Herança

# Herdando pizzas ツ

class Pizza:
    pedacos = 8
    
    @classmethod
    def quant_pedacos(cls, quantidade):
        cls.pedacos = quantidade
    

# Classe Mussarela herdando a classe Pizza
# Herança "simples"
class Mussarela(Pizza):
    pass    
    
class Calabresa(Pizza):
    pass

# Herança "multipla"
class DoisSabores(Mussarela, Calabresa):
    pass