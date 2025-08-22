import os 
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

class Animal:
    
    def hacer_sonido(self):
        pass

class Mamifero(Animal):
    
    def hacer_sonido(self):
        return "Sonido de mamífero"

class Ave(Animal):
    
    def hacer_sonido(self):
        return "Sonido de ave"
    
class Reptil(Animal):

    def hacer_sonido(self):
        return "Sonido de reptil"

def sonidos_animales(ser_vivo):
    print(ser_vivo.hacer_sonido())
    
mamifero = Mamifero()
sonidos_animales(mamifero)

ave = Ave()
sonidos_animales(ave)

reptil = Reptil()
sonidos_animales(reptil)