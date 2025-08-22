# Definimos una clase padre
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacio
        pass
    # Método genérico pero con implementación particular
    def moverse(self):
        #metodo vacio
        pass
    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    def __init__(self, especie, edad, dueño, raza, nombre):
        # Alternativa 1
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño
    # Alternativa 2
        super().__init__(especie, edad)
        self.dueño = dueño
        self.raza = raza
        self.nombre = nombre
        print(f"Su nombre es {nombre}, su raza es {raza} tiene unos {edad} añitos ah y por cierto su dueño es {dueño} yo solo lo cuido")
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Camina en 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("buzzz")
    def moverse(self):
        print("Volando")
    #Nuevo metodo
    def picar(self):
        print("Picar")

print(Perro.__bases__)
# (<class '__main__.Animal'>,)
print(Animal.__subclasses__())
# [<class '__main__.Perro'>]

mi_perro = Perro("mamifero", 10, "Pedro", "ladrador", "Toby")
mi_perro.describeme()
print(type(mi_perro))
# deberia decir: soy un animal del tipo perro
mi_vaca = Vaca("mamifero", 23)
mi_abeja = Abeja("insecto", 1)

mi_vaca.hablar()
mi_vaca.describeme()
mi_abeja.describeme()
mi_abeja.picar()
