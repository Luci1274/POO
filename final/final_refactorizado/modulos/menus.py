import sys
import os
import platform
from tabulate import tabulate
from modulos.login import Login
from modulos.apis.dog_api import abrir_imagen
from modulos.apis.joke_api import traducir_chiste
from modulos.apis.dolar_api import Dolar_oficial, Dolar_tarjeta, Dolar_blue


def clear():
    "Limpia la pantalla y hace unas lineas"
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print("-" * 50)


class Menu_base:
    def __init__ (self):
        self.clear = clear()
    
    def opciones_menu(self):
        print()
        ver_opciones = [[]]
        print(tabulate(ver_opciones,tablefmt="fancy_grid"))
    
    def elegir_opcion(self):
        elegir = input("Por favor ingrese el numero de la opcion deseada: ").strip()
        return elegir
    
    def verificacion_opcion(self):
        pass
    
    def ejeutar(self):
        while True:
            self.clear
            self.opciones_menu()
            elegir = self.elegir_opcion()
            resultado = self.verificacion_opcion()
            
class Menu_login(Menu_base):
    def __init__(self):
        self.clear = clear()
        self.login = Login()
    
    def opciones_menu(self):
        print("Bienvenido al final de Programacion 1.")
        ver_opciones = [["1. Iniciar sesion"],["2. Registrarse"],["3. Salir"]]
        print(tabulate(ver_opciones,tablefmt="fancy_grid"))

    def verificar_opcion(self, elegir):
        if elegir == "1":
            resultado = self.login.ingresar_usuario()
            if resultado != None:
                return resultado
            else:
                return None

        elif elegir == "2":
            if self.login.registrar_usuario() == True:
                print("Inicio exitoso")      
                
            return None
        elif elegir == "3":
            print("Finalizando programa...")
            sys.exit(0)
        else:
            print("Opcion invalida, por favor ingrese una valida")
            return None
    
    def ejecutar(self):
        while True:
            clear()
            self.opciones_menu()
            elegir = self.elegir_opcion()
            resultado = self.verificar_opcion(elegir)
            if resultado != None:
                return resultado
            else:
                continue
            
class Menu_usuario(Menu_base):
    def __init__(self):
        self.clear = clear()
        self.abrir_imagen = abrir_imagen
        self.traducir_chiste = traducir_chiste
        self.menu_dolar = Menu_dolar()
    
    def opciones_menu(self):
        print("Bienvenido a pruebas api, Por favor vea las opciones")
        ver_opciones_menu = [["1. Fotos de perros"],["2. chistes"],["3. Dolar"] ,["4. cerrar sesion"]]
        print(tabulate(ver_opciones_menu,tablefmt="fancy_grid"))
        return
    
    def verificar_opcion(self, opcion):
        self.clear
        if opcion == "1":
            abrir_imagen()
            input("Presione enter para continuar")
            ultima_pagina_visitada = "Api perros"
            return ultima_pagina_visitada
        elif opcion == "2":
            traducir_chiste()
            input("Presione enter para continuar") 
            ultima_pagina_visitada = "Api chistes"
            return ultima_pagina_visitada   
        elif opcion == "3":
            self.menu_dolar.ejecutar()
            ultima_pagina_visitada = "Api dolar"
            return ultima_pagina_visitada
        elif opcion == "4":
            print("Gracias por participar en esta prueba")
            return None
        else:
            print("Opcion incorrecta intente nuevamente")
            input("Presione enter para continuar")
            return True
    
    def ejecutar(self):
        nuevo_ingreso = 1
        paginas_visitadas = 0
        paginas = []
        while True:
            self.clear
            self.opciones_menu()
            opcion = self.elegir_opcion()
            pagina = self.verificar_opcion(opcion)
            paginas.append(pagina)
            if  len(paginas) == 1 and paginas[0] == None:
                ultima_pagina_visitada = "salir"
                return nuevo_ingreso, paginas_visitadas, ultima_pagina_visitada
            elif len(paginas) > 1 and paginas[-1] == None:
                ultima_pagina_visitada = paginas[-2]
                return nuevo_ingreso, paginas_visitadas, ultima_pagina_visitada
            else:
                paginas_visitadas += 1
                continue

class Menu_dolar(Menu_base):
    def __init__(self):
        self.clear = clear()
        self.Dolar_oficial = Dolar_oficial
        self.Dolar_tarjeta = Dolar_tarjeta
        self.Dolar_blue = Dolar_blue
    
    def opciones_menu(self):
        print("Ingrese una de estas opciones: ")
        ver_opciones_dolar = [["1. Dolar oficial"],["2. Dolar tarjeta"],["3. Dolar Blue"] ,["4. Regresar"]]
        print(tabulate(ver_opciones_dolar,tablefmt="fancy_grid"))
    
    def verificar_opcion(self, opcion):
        while True:
            self.clear
            if opcion == "1":
                dolar_oficial = Dolar_oficial()
                dolar_oficial.mostrar_info()
                input("Presione enter para continuar")
                break
            
            elif opcion == "2":
                dolar_tarjeta = Dolar_tarjeta()
                dolar_tarjeta.mostrar_info()
                input("Presione enter para continuar")
                break
            
            elif opcion == "3":
                dolar_blue = Dolar_blue()
                dolar_blue.mostrar_info()
                input("Presione enter para continuar")
                break

            elif opcion == "4":
                print("Regresando al menu principal")
                break
            
            else:
                print("Opcion incorrecta intente nuevamente")
                input("Presione enter para continuar")

    def ejecutar(self):
        self.clear
        self.opciones_menu()
        opcion = self.elegir_opcion()
        self.verificar_opcion(opcion)
        return