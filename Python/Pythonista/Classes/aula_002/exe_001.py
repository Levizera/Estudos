# --> Anotações
# --> Todas as intancias vão compartilhar da "c_fila", pois ela é um objeto da classe em si, e não de uma instância. Uma variavel "Global" e não local como uma instância.

class Fila:
    # Fila é uma asbtração de várias coisas
    # 	- Processos
    # 	- Fila de supermercado 
    # 	- Ou uma fila de qualquer outra coisa
    
    c_fila = []
    # c_fila é um objeto/variavel da classe
    # é basicamente como se fosse uma váriavel global
    
    @classmethod # --> serve para "dizer" que ali vai ser trabalhado um objeto da classe
    def c_entrar(cls, obj): # cls --> se refere à classe e aos seus objetos
    	cls.c_fila.append(obj)
    	print(cls.c_fila)
    
    # Esse metodo pode ser usado sem ter que instância-lo
    # Assim como tambem pode ser acessado se caso fort instânciaodo
    
    
    def __init__(self):
    	self.s_fila = []
    # s_fila só pode ser acessada pela classe
    # Apartir do momento em que ela for instânciada
    # em um metodo. Por isso que temos o __init__, que é um inicializador de classe ou instância
    # e com o "self" é possivel criar variveis dentro de um metodo
    
    def s_entrar(self, obj):
        self.s_fila.append(obj)
        print(self.s_fila)