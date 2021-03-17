class Clientes:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def Todas_as_infos(self):
        print(self.nome, self.sobrenome, self.idade)
        

c1 = Clientes('Levi', 'Ferreira', '17')
c2 = Clientes('Pedro', 'Silva', '16')
c3 = Clientes('Lucas', 'Dionisio', '17')


class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def comer(self, alimento):
        if self.comendo:
            print(f' {self.nome} Já está comendo... ')
            return
        
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
        
    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
            
        print(f'{self.nome} parou de comer!!')
        self.comendo = False
        
pessoa1 = Pessoa('Levi', 17)
pessoa2 = Pessoa('Pedro', 16)