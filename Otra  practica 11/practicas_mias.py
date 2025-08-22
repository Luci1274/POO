import os
def clear():
    try:
        os.system("cls")
        os.system("clear")
        print("-" * 50)
    except:
        pass

class Vehiculo:
    def __init__ (self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelererar(self, nueva_velocidad):
        print(f"El vehiculo va a {self.velocidad}km")
        if nueva_velocidad > self.velocidad:
            self.velocidad = nueva_velocidad
            print(f"Y aceleró a {self.velocidad}km")
        else:
            print("Como ingreso un valor menor al actual, cambiando a la accion disminuir")
            self.disminuir(nueva_velocidad)

    def disminuir(self, nueva_velocidad):
        if nueva_velocidad < self.velocidad:
            self.velocidad = nueva_velocidad
            print(f"El vehiculo disminuyo a {self.velocidad}km")
        else:
            print("Como ingreso un valor mayor al actual cambiando a la accion acelerar")
            self.acelererar(nueva_velocidad)
    
    def informacion(self):
        print(f"El vehiculo cuenta con la siguiente información: \n marca: {self.marca}\n modelo: {self.modelo}\n velocidad actual {self.velocidad}km")

class Auto(Vehiculo):
    
    def acelererar(self, nueva_velocidad):
        super().acelererar(nueva_velocidad)
        print("Recuerde transitar con cuidado, muchas gracias")
    
class Camion(Vehiculo):
    
    def acelererar(self, nueva_velocidad):
        super().acelererar(nueva_velocidad)
        print("Recuerde que la velocidad maxima de los camiones es 60km")
    
class Moto(Vehiculo):
    def __init__(self, marca, modelo, velocidad):
        super().__init__(marca, modelo, velocidad)

def continuar():
    print("quieres continuar? S/N")
    c = input("").lower().strip()
    if c != "s":
        return False
    else:
        return True

def ingresar_datos():
    clear()
    marca = input("Ingrese una marca: ").lower().strip()
    modelo = input("Ingrese un modelo: ").lower().strip()
    while True:
        try:    
            velocidad = int(input("Ingrese la velocidad actual: ").strip())
            if velocidad > 0:
                return marca, modelo, velocidad
            else:
                print("Ingrese una velocidad mayor a 0 ")
        except:
            print("Ingrese un valor numerico valido")

def acciones(a):
    clear()
    while True:
        print("Opciones a realizar 1: ver informacion, 2: aumentar velocidad, 3: disminuir velocidad, 4: ir a la seleccion de vehiculos")
        opcion = input("").lower().strip()
        if opcion == "1":
            a.informacion()
            if continuar() == True:
                continue
            else:
                elegir_vehiculo()

        elif opcion == "2":
            nueva_velocidad = cambiar_velocidad()
            a.acelererar(nueva_velocidad)
            if continuar() == True:
                continue
            else:
                elegir_vehiculo()

        elif opcion == "3":
            nueva_velocidad = cambiar_velocidad()
            a.disminuir(nueva_velocidad)
            if continuar() == True:
                continue
            else:
                elegir_vehiculo()

        elif opcion == "4":
            break
        else:
            print("Ingreso invalido, por favor ingrese un valor valido")

def cambiar_velocidad():
    while True:
        try:
            nueva_velocidad = int(input("Ingrese una nueva velocidad: "))
            return nueva_velocidad
        except:
            print("Por favor ingrese una velocidad")
            continue

def elegir_vehiculo():
    while True:
        clear()
        print("Elige el tipo de vehiculo 1: auto, 2: Camion, 3: Moto, 4: finalizar programa")
        opcion = input("").lower().strip()
        if opcion == "1":
            marca, modelo, velocidad = ingresar_datos()
            auto = Auto(marca, modelo, velocidad)
            acciones(auto)
            if continuar() == True:
                continue
            else:
                elegir_vehiculo()

        elif opcion == "2":
            marca, modelo, velocidad = ingresar_datos()
            camion = Camion(marca, modelo, velocidad)
            acciones(camion)
            if continuar() == True:
                continue
            else:
                elegir_vehiculo()

        elif opcion == "3":
            marca, modelo, velocidad = ingresar_datos()
            moto = Moto(marca, modelo, velocidad)
            acciones(moto)
            if continuar() == True:
                continue
            else:
                elegir_vehiculo()

        elif opcion == "4":
            exit()
        else:
            print("Ingrese un valor valido")

clear()
elegir_vehiculo()