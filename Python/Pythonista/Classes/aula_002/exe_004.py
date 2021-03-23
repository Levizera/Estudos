# Brincando com Heranças

class Pizza:
    pedacos = 8
    
    @classmethod
    def quant_pedacos(cls, quantidade):
        cls.pedacos = quantidade
    
class Mussarela(Pizza):
    pass
    
class Portuguesa(Pizza):
    pass

class MeioAMeio(Mussarela, Portuguesa):
    pass