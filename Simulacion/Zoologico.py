import random

def clear():
    clear = print("\n" * 25, "-" * 50)
    return clear

class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.animales = ["mono", "foca"]

    def agregar_animal(self, animal):
        if animal not in self.animales:
            self.animales.append(animal)
            print(f"El animal: {animal} fue agregado")
        else:
            print("El animal ya fue agregado con anterioridad")
    
    def eliminar_animal(self, animal):
        if animal in self.animales:
            self.animales.pop(animal)
        else:
            print("El animal no está en el zoologico")
    
    def buscar_animal(self, animal):
        if animal in self.animales:
            for a in self.animales:
                if a == animal:
                    return animal
        else:
            print("El animal no está en el zoologico")

    def mostrar_animales(self):
        for animal in self.animales:
            print(f"{animal}")

class Animal:
    def __init__ (self, especie):
        self.nombre = random.choice(["Lisa", "Frank", "Gabriel", "Mikaela", "Princesa", "Ale"])
        self.edad = random.choice([3, 4, 8, 9, 2, 5])
        self.especie = especie
        self.salud = random.choice(["Buen", "Regular", "Mal"])
    
    def mostrar_info(self):
        print("-" * 50)
        print(f"El/Ella es de la especie {self.especie}\n Su nombre es {self.nombre}\n Tiene {self.edad} años\n Y está {self.salud} de salud")
    
    def actualizar_salud(self, nueva_salud):
        print(f"Cambiando el estado de salud a {nueva_salud}")
        self.salud = nueva_salud
        self.mostrar_info()
        self.salud = random.choice(["Buen", "Regular", "Mal"])

class Animal_exotico(Animal):
    def __init__(self, especie):
        super().__init__(especie)
        self.pais_origen = random.choice(["Argentina", "Alemania", "China", "Africa", "Rusia", "Madagascar"])
        self.nivel_riesgo = random.choice(["Bajo","Medio"," Alto"])
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Este animal es originario de {self.pais_origen}\n Y su nivel de riesgo es: {self.nivel_riesgo}")


def elegir(zoologico):
    while True:
        clear()
        print("Seleccione el numero de la accion desea realizar\n 1: zoologico\n 2: animal\n 3: animal exotico")
        elegir = input("").lower().strip()
        if elegir == "1" or elegir == "agregar animal":
            elegir_accion_zoologico(zoologico)
            return zoologico
        elif elegir == "2" or elegir == "animal":
            zoologico.mostrar_animales()
            especie = input("Escriba la especie del animal: ")
            if especie in zoologico.animales:
                animal = Animal(especie)
                elegir_accion_animal(animal)
                return animal
            else:
                print("Especie de animal equivocada, por favor ingrese otra")
                input("Precione enter para continuar")
        elif elegir == "3" or elegir == "animal exotico":
            zoologico.mostrar_animales()
            especie = input("Escriba la especie del animal: ")
            if especie in zoologico.animales:
                animal_exotico = Animal_exotico(especie)
                elegir_accion_animal(animal)
                return animal_exotico
            else:
                print("Especie de animal equivocada, por favor ingrese otra")
                input("Precione enter para continuar")

def elegir_accion_zoologico(zoologico):
    while True:
        clear()
        print("Seleccione el numero de la accion desea realizar\n 1: Agregar animal\n 2: Eliminar animal\n 3: Buscar animal\n 4: mostrar animales")
        elegir = input("").lower().strip()        
        if elegir == "1" or elegir == "agregar animal":
            agregar_animal(zoologico)
            return
        elif elegir == "2" or elegir == "eliminar animal":
            eliminar_animal(zoologico)
            return
        elif elegir == "3" or elegir == "buscar animal":
            buscar_animal(zoologico)
            return
        elif elegir == "4" or elegir == "mostrar animales":
            zoologico.mostrar_animales()
            return

def agregar_animal(a):
    clear()
    especie_animal = input("Agregue la espcie del animal: ")
    a.agregar_animal(especie_animal)

def eliminar_animal(a):
    clear()
    a.mostrar_animales()
    eliminar = input("Por favor escriba el animal que desea eliminar ")
    if eliminar in a.animales:
        a.eliminar_animal(eliminar)
    else:
        print("El animal ingresado no está registado")

def buscar_animal(a):
    clear()
    a.mostrar_animales()
    buscar = input("Por favor ingresa el animal a buscar ")
    if buscar in a.animales:
        a.buscar_animal(buscar)
    else:
        print("El animal ingresado no está registrado")

def elegir_accion_animal(animal):
    while True:
        clear()
        print("Seleccione el numero de la accion desea realizar\n 1: Mostrar info\n 2: Modificar salud")
        elegir = input("").lower().strip()
        if elegir == "1" or elegir == "mostrar info":
            mostrar_info(animal)
            return
        elif elegir == "2" or elegir == "Modificar salud":
            modificar_salud(animal)
            return

def modificar_salud(a):
    clear()
    nueva_salud = input("Escriba la nueva salud del animal ")
    a.actualizar_salud(nueva_salud)
    
def mostrar_info(animal):
    clear()
    animal.mostrar_info()

zoologico = Zoologico("Central Park", "Italia")

while True:
    elegir(zoologico)
    continuar = input("Desea continuar? s/n ").lower().strip()
    if continuar == "s" or continuar == "si" or continuar == "yes" or continuar == "y":
        continue
    else:
        print("Muchas gracias por su tiempo")
        exit()