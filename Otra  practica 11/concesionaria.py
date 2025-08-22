#sistema de gestion de una concesionaria (somos un trabajador)

import os
import random

def clear():
    clear = os.system("cls")
    print("-" * 50)

class Vehiculo:
    def __init__ (self, marca, modelo, año_modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.año_modelo = año_modelo
        self.precio = precio
    
    def info(self):
        return

class Auto(Vehiculo):
    def __init__ (self, marca, modelo, año_modelo, precio, cantidad_puertas, cantidad_asientos, nueva):
        super().__init__(marca, modelo, año_modelo, precio)
        self.cantidad_puertas = cantidad_puertas
        self.cantidad_asientos = cantidad_asientos
        self.nueva = nueva
    
    def info(self):
        
        print("-" * 50)
        print(f"\n Las caracteristicas del auto son:\n"
        f"Marca: {self.marca}\n"
        f"Modelo: {self.modelo}\n"
        f"Año del modelo: {self.año_modelo}\n"
        f"Precio: {self.precio}\n"
        f"Cantidad de puertas: {self.cantidad_puertas}\n"
        f"Cantidad de asientos: {self.cantidad_asientos}\n"
        f"Es nuevo? {self.nueva}\n")
        print("-" * 50)

class Moto(Vehiculo):
    def __init__ (self, marca, modelo, año_modelo, precio, nueva):
        super().__init__(marca, modelo, año_modelo, precio)
        self.nueva = nueva
    
    def info(self):
        
        print("-" * 50)
        print(f"\n Las caracteristicas del auto son:\n"
        f"Marca: {self.marca}\n"
        f"Modelo: {self.modelo}\n"
        f"Año del modelo: {self.año_modelo}\n"
        f"Precio: {self.precio}\n"
        f"Es nuevo? {self.nueva}\n")
        print("-" * 50)

class Concesionaria:
    def __init__(self):
        self.autos = {}
        self.motos = {}

    def mostrar_autos(self):
        print("-" * 50)
        print("Los autos disponibles son:")
        for marca in self.autos.keys():
            print(f"Marca: {marca}")
        print("-" * 50)

    def mostrar_motos(self):
        print("-" * 50)
        print("Las motos disponibles son:")
        for marca in self.motos.keys():
            print(f"Marca: {marca}")
        print("-" * 50)

    def registrar_auto(self):
        marca = input("Por favor ingrese la marca del Vehiculo: ").strip().lower()
        modelo = input("Por favor ingrese el modelo del Vehiculo: ").strip().lower()
        año_modelo = input("Por favor ingrese el año del modelo: ").strip()

        while True:
            try:
                precio = int(input("Por favor ingrese el precio del Vehiculo: "))
                if precio > 0:
                    break
                else:
                    print("Por favor ingrese un valor mayor a 0")
            except:
                print("Por favor ingrese un valor numerico")

        cantidad_puertas = input("Por favor ingrese la cantidad de puertas del Vehiculo: ").strip()
        cantidad_asientos = input("Por favor ingrse la cantidad de asientos: ")

        while True:
            nueva = input("El Vehiculo es nuevo?: ").lower().strip()
            if nueva == "si" or nueva == "no":
                if nueva == "no":
                    # Aplica un descuento del 20% si no es nuevo
                    precio = int(precio * 0.8)
                break
            else:
                print("Por favor solo ingrese si o no")

        auto = Auto(marca, modelo, año_modelo, precio, cantidad_puertas, cantidad_asientos, nueva)
        if marca not in self.autos:
            self.autos[marca] = (modelo, año_modelo, precio, cantidad_puertas, cantidad_asientos, nueva)
            print("Auto registrado con exito")
            return auto
        else:
            print("El auto ya fue registrado con anterioridad")

    def registrar_moto(self):
        marca = input("Por favor ingrese la marca del Vehiculo: ").strip().lower()
        modelo = input("Por favor ingrese el modelo del Vehiculo: ").strip().lower()
        año_modelo = input("Por favor ingrese el año del modelo: ").strip()

        while True:
            try:
                precio = int(input("Por favor ingrese el precio del Vehiculo: "))
                if precio > 0:
                    break
                else:
                    print("Por favor ingrese un valor mayor a 0")
            except:
                print("Por favor ingrese un valor numerico")

        while True:
            nueva = input("El Vehiculo es nuevo?: ").lower().strip()
            if nueva == "si" or nueva == "no":
                if nueva == "no":
                    # Aplica un descuento del 20% si no es nueva
                    precio = int(precio * 0.8)
                break
            else:
                print("Por favor solo ingrese si o no")

        moto = Moto(marca, modelo, año_modelo, precio, nueva)
        if marca not in self.motos:
            self.motos[marca] = (modelo, año_modelo, precio, nueva)
            print("La Moto fue registrada con exito")
            return moto
        else:
            print("La moto ya fue registrada con anterioridad")

    def venta_auto(self):
        self.mostrar_autos()
        elegir = input("Ingrese la marca del auto a vender: ").lower().strip()
        if elegir in self.autos:
            saldo = random.choice([True, False])
            if saldo:
                datos = self.autos[elegir]
                print(f"El Auto Marca: {elegir}, Modelo: {datos[0]} ha sido vendido con éxito")
                self.autos.pop(elegir)
            else:
                print("Saldo insuficiente para realizar la venta")
        else:
            print("La marca ingresada no está disponible, regresando al menú")

    def venta_moto(self):
        self.mostrar_motos()
        elegir = input("Ingrese la marca de la moto a vender: ").lower().strip()
        if elegir in self.motos:
            saldo = random.choice([True, False])
            if saldo:
                datos = self.motos[elegir]
                print(f"La Moto Marca: {elegir}, Modelo: {datos[0]} ha sido vendida con éxito")
                self.motos.pop(elegir)
            else:
                print("Saldo insuficiente para realizar la venta")
        else:
            print("La marca ingresada no está disponible, regresando al menú")


def elegir_opcion():
    clear()
    print("Bienvenido a runrun Por favor elige una de las siguientes opciones")
    print("Ingrese el numero de la opcion elegida")
    print("1 Registrar un Auto") 
    print("2 Registrar una Moto")
    print("3 Mostrar Autos")
    print("4 Mostrar Motos")
    print("5 Vender Auto")
    print("6 Vender Moto")
    print("7 Salir")
    print("-" * 50)
    elegir = input("").lower().strip()
    return elegir


def menu():
    concesionaria = Concesionaria()
    while True:
        elegir = elegir_opcion()

        if elegir == "1":
            auto = concesionaria.registrar_auto()
            continuar()

        elif elegir == "2":
            moto = concesionaria.registrar_moto()
            continuar()

        elif elegir == "3":
            concesionaria.mostrar_autos()
            continuar()

        elif elegir == "4":
            concesionaria.mostrar_motos()
            continuar()

        elif elegir == "5":
            concesionaria.venta_auto()
            continuar()

        elif elegir == "6":
            concesionaria.venta_moto()
            continuar()

        elif elegir == "7":
            break

        else:
            print("Por favor ingrese el valor numero de la opcion")
            continuar()

def continuar():
    input("Presione enter para continuar")
        
menu()