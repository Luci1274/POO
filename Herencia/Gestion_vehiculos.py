import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        print(f"La marca del vehiculo es: {self.marca}, el modelo es: {self.modelo}")

class Automovil(Vehiculo):

    def __init__ (self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo)
        self.numro_puertas = numero_puertas
    
    def mostrar_informacion(self):
        print(f"\nA continuacion hablaremos de un automovil")
        super().mostrar_informacion()
        print(f" Y su numero de puertas es: {self.numro_puertas}")


vehiculo = Vehiculo("corola", 2004)
vehiculo.mostrar_informacion()

automovil = Automovil("corola", 2004, 4)
automovil.mostrar_informacion()