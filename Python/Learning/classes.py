# Para mostrar as "Configuracoes" da classe: 
# --> celular1.Configuracoes()

class Celulares:
    def __init__(self, marca, ram, preco, cor):
        self.marca = marca
        self.cor = cor
        self.ram = ram
        self.preco = preco
        
    def Ligar(self):
        print('Ligado')
    
    def Desligado(self):
        print('Desligado')
    
    def Configuracoes(self):
        print(self.marca, self.ram, self.preco, self.cor)

celular1 = Celulares('Apple', '4GB', 4000, 'Preto')
celular2 = Celulares('Samsung', '6GB', 4500, 'Branco')
celular3 = Celulares('Xiaomi', '4GB', 3100, 'Vermelho')


class Robo:
    def __init__(self, tamanho, material, peso):
        self.tamanho = tamanho
        self.material = material
        self.peso = peso
        
    def Modo_de_batalha(self):
        print('Entrando em modo de Batalha...')
        
    def Desativando(self):
        print('Desativando modo de batalha em 3...2...1...')
        
    def Componenetes(self):
        print(self.tamanho, self.material, self.peso)

    
robo_Jimmy = Robo('1m', 'Aço', '1.1Kg')
robo_Gimble = Robo('90cm', 'Ferro', '980gm')
robo_Grey = Robo('1.2m', 'Aluminio', '1.5Kg')