import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

import tabulate

class Vehiculo:
    def __init__ (self, tipo, marca, modelo, matricula, color):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.color = color
    
    def Mostrar_informacion(self):
        informacion = {"Tipo": self.tipo, "Marca": self.marca, "Modelo": self.modelo, "Matrícula": self.matricula, "Color": self.color}
        for item, valor in informacion.items():
            print(f"{item}: {valor}")

class Auto(Vehiculo):

    def Mostrar_informacion(self):
        linea_separadora = "-" * 80
        print(linea_separadora)
        super().Mostrar_informacion()
        print("Características adicionales: 4 ruedas, motor de combustión interna")
        print(linea_separadora)


class Moto(Vehiculo):

    def Mostrar_informacion(self):
        linea_separadora = "-" * 80
        print(linea_separadora)
        super().Mostrar_informacion()
        print("Características adicionales: 2 ruedas, motor de combustión interna")
        print(linea_separadora)

class Camion(Vehiculo):
    
    def Mostrar_informacion(self):
        linea_separadora = "-" * 80
        print(linea_separadora)
        super().Mostrar_informacion()
        print("Características adicionales: 6 ruedas, motor de combustión interna")
        print(linea_separadora)

def mostrar_informacion_vehiculo(vehiculo):
    vehiculo.Mostrar_informacion()

def seleccionar_vehiculo():
    vehiculos = {1: "Auto", 2: "Moto", 3: "Camión"}
    print(f"Seleccione el tipo de vehículo \n{tabulate.tabulate(vehiculos.items(), headers=['Número', 'Tipo de Vehículo'], tablefmt='grid')}")
    while True:
        try:
            opcion = int(input("Ingrese el número de la opción: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")
            clear()
            continue
        if opcion in vehiculos:
            print(f"Usted ha seleccionado: {vehiculos[opcion]}")
            input("Presione Enter para continuar...")
            clear()
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            clear()
    return opcion

opcion = seleccionar_vehiculo()
if opcion == 1: 
    auto = Auto("Auto", "Toyota", "Corolla", "ABC123", "Rojo")
    mostrar_informacion_vehiculo(auto)

elif opcion == 2:
    moto = Moto("Moto","Honda", "CBR80R", "XYZ789", "Negro")
    mostrar_informacion_vehiculo(moto)

else:
    camion = Camion("Camion","Mercedes-Benz", "Actros", "LMN456", "Blanco")
    mostrar_informacion_vehiculo(camion)
