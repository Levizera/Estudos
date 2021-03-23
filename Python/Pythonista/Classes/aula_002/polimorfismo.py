class Pizza:
    pedacos = 8
    
    @classmethod
    def quant_pedacos(cls, quantidade):
        cls.pedacos = quantidade
    
    @staticmethod
    def ingredientes():
        return 'Ingredientes'
        
        
class Mussarela(Pizza):
    
    @staticmethod
    def ingredientes():
        return ['Queijo Mussarela', 'Massa', 'Molho de Tomate', 'Oregano']
    
