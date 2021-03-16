class Pet:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def greeting(self):
        print(f'Hello im {self.name}, and im {self.age} years old ')

# Adicionando caracteristicas a um pet em especifico        
class Cat(Pet):
    def __init__(self, name, age, color):
        self.color = color
        
    def speak(self):
        print('Meow Meow')
        
class Dog(Pet):
    def speak(self):
        print('Hoof Hoof')
        
        
me = Pet('Levi', 17)    #   me.greeting()
gato = Cat('Xanin', 2, 'Branco')  #   gato.greeting()
cachorro = Dog('Campeão', 4)    #   cachorro.greeting()