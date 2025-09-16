import sys
import os
import platform
from tabulate import tabulate
from modulos.login import Login
from modulos.apis.dog_api import abrir_imagen
from modulos.apis.joke_api import traducir_chiste
from modulos.apis.dolar_api import Dolar_oficial, Dolar_tarjeta, Dolar_blue
from time import sleep


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
    
    def ejecutar(self):
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
        ver_opciones = [["1. Iniciar sesion"], ["2. Registrarse"], ["3. Cambiar contraseña"], ["4. Salir"]]
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
        
        elif elegir == "3":
            self.login.cambiar_contraseña()
                
            return None
        elif elegir == "4":
            print("Finalizando programa...")
            sleep(1)
            clear()
            sys.exit(0)
        else:
            print("Opcion invalida, por favor ingrese una valida")
            return None
    
    def EULA(self):
        print(
        "📜 Acuerdo de Usuario Final (EULA)\n"
        "\n"
        "Bienvenido al sistema. Antes de continuar, por favor lea atentamente los siguientes términos:\n"
        "\n"
        "1. Al iniciar sesión, usted acepta que sus datos serán almacenados con fines estrictamente académicos,\n"
        "   anecdóticos y, eventualmente, para engrosar su currículum en el futuro.\n"
        "2. El sistema no se hace responsable si su nombre aparece en una lista de 'usuarios ejemplares'\n"
        "   o 'quienes borraron su cuenta en menos de 5 minutos'.\n"
        "3. Al interactuar con las APIs, usted acepta que sus gustos por perros, chistes malos y cotizaciones del dólar\n"
        "   quedarán registrados para la posteridad.\n"
        "4. Si decide eliminar su cuenta, el sistema lo respetará... pero no lo olvidará.\n"
        "5. Este sistema no comparte sus datos con terceros, excepto con su profesor, su conciencia\n"
        "   y algún algoritmo curioso que quiere aprender de usted.\n"
        "6. Al presionar 'Aceptar', usted declara que ha leído, comprendido y probablemente ignorado todo lo anterior.\n"
        "\n"
        "¿Acepta los términos y condiciones?\n"
        "🟢 Sí, quiero que mi historial sea parte de mi legado académico.\n"
        "🔴 No, pero igual voy a entrar porque quiero ver el chiste del día.\n"
        )
        decision_EULA = input("S/N: ").strip().upper()
        if decision_EULA != "S":
            return False
        else:
            return True
    
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
        ver_opciones_menu = [["1. Fotos de perros"],["2. chistes"],["3. Dolar"]]
        ver_opciones_menu.append([str(len(ver_opciones_menu) + 1) + ". Para borrar la cuenta"])
        ver_opciones_menu.append([str(len(ver_opciones_menu) + 1) + ". Para salir"])
        print(tabulate(ver_opciones_menu,tablefmt="fancy_grid"))
        return ver_opciones_menu
    
    def verificar_opcion(self, opcion, ver_opciones_menu):
        self.clear
        if opcion == "1":
            abrir_imagen()
            input("Presione enter para continuar")
            ultima_api_visitada = "Api perros"
            return ultima_api_visitada
        elif opcion == "2":
            traducir_chiste()
            input("Presione enter para continuar") 
            ultima_api_visitada = "Api chistes"
            return ultima_api_visitada   
        elif opcion == "3":
            self.menu_dolar.ejecutar()
            ultima_api_visitada = "Api dolar"
            return ultima_api_visitada
        elif opcion == str(len(ver_opciones_menu) - 1):
            verificar = input("Presione borrar cuenta ¿Está seguro? S/N: ").strip().upper()
            if verificar == "S" or verificar == "SI" or verificar == "YES":
                return "Eliminar"
            else:
                return "Salir"
                
        elif opcion == str(len(ver_opciones_menu)):
            print("Gracias por participar en esta prueba")
            return None
        else:
            print("Opcion incorrecta intente nuevamente")
            input("Presione enter para continuar")
            return "Error"
    
    def ejecutar(self):
        nuevo_ingreso = 1
        apis_visitadas = 0
        apis = []
        while True:
            self.clear
            ver_opciones_menu = self.opciones_menu()
            opcion = self.elegir_opcion()
            api = self.verificar_opcion(opcion, ver_opciones_menu)
            apis.append(api)
            if  len(apis) == 1 and apis[0] == "Salir":
                ultima_api_visitada = "ninguna"
                return nuevo_ingreso, apis_visitadas, ultima_api_visitada, False
            elif len(apis) == 1 and apis[0] == "Eliminar":
                ultima_api_visitada = "ninguna"
                return nuevo_ingreso, apis_visitadas, ultima_api_visitada, True
            elif len(apis) > 1 and apis[-1] == "Salir":
                ultima_api_visitada = apis[-2]
                return nuevo_ingreso, apis_visitadas, ultima_api_visitada, False
            elif len(apis) > 1 and apis[-1] == "Eliminar" and apis[-2] != "Error":
                ultima_api_visitada = apis[-2]
                return nuevo_ingreso, apis_visitadas, ultima_api_visitada, True
            else:
                apis_visitadas += 1
                continue

class Menu_dolar(Menu_base):
    def __init__(self):
        self.clear = clear()
        self.Dolar_oficial = Dolar_oficial
        self.Dolar_tarjeta = Dolar_tarjeta
        self.Dolar_blue = Dolar_blue
    
    def opciones_menu(self):
        print("Ingrese una de estas opciones: ")
        ver_opciones_dolar = [["1. Dolar oficial"],["2. Dolar tarjeta"],["3. Dolar Blue"]]
        ver_opciones_dolar.append([str(len(ver_opciones_dolar) + ". regresar")])
        print(tabulate(ver_opciones_dolar,tablefmt="fancy_grid"))
        return ver_opciones_dolar
    
    def verificar_opcion(self, opcion, ver_opciones_dolar):
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

            elif opcion == str(len(ver_opciones_dolar)):
                print("Regresando al menu principal")
                break
            
            else:
                print("Opcion incorrecta intente nuevamente")
                input("Presione enter para continuar")

    def ejecutar(self):
        self.clear
        ver_opciones_dolar = self.opciones_menu()
        opcion = self.elegir_opcion()
        self.verificar_opcion(opcion, ver_opciones_dolar)
        return