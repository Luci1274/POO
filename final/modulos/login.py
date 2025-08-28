import sys
from tabulate import tabulate
import os
import platform
from modulos.manipular_archivos import GestorDatos

def clear():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("-" * 50)

class Login:
    def __init__(self):
        self.gestor = GestorDatos()
    
    def ingresar_usuario(self):
        fallos = 0
        while True:
            clear()
            print("Para iniciar sesion por favor ingrese el nombre de usuario y contraseña")
            nombre_usuario = input("Nombre de usuario: ").strip()
            contraseña = input("Contraseña: ").strip()
            if len(nombre_usuario) == 0 or len(contraseña) == 0:
                print("Por favor rellene los campos")
                input("Presione enter para continuar")
                continue
            elif self.verificar_usuario(nombre_usuario, contraseña) == True: 
                print("Inicio exitoso")
                usuario = Usuario(nombre_usuario, contraseña)
                return nombre_usuario, False
            elif self.verificar_admin(nombre_usuario, contraseña) == True: 
                print("Inicio exitoso bienvenido señor")
                input("Presione enter para continuar")
                return True
            else:
                print("Usuario o contraseña inocrrecta, por favor intente nuevamente")
                input("Presione enter para continuar")
                fallos += 1
                if fallos == 3:
                    print("Demasiados fallos, volviendo al menu")
                else:
                    continue
            

    def verificar_usuario(self, nombre_usuario, contraseña):
        ruta_usuario = "modulos\\archivos\\usuarios.json"
        respuesta = self.gestor.verificar_credenciales(ruta_usuario, nombre_usuario, contraseña)
        return respuesta

    def verificar_admin(self, nombre_usuario, contraseña):
        ruta_admin = "modulos\\archivos\\administradores.json" 
        respuesta = self.gestor.verificar_credenciales(ruta_admin, nombre_usuario, contraseña)
        return respuesta

    def registrar_usuario(self):
        fallos = 0
        while True:
            clear()
            print("Por favor llene los siguientes espacios para crear un usuario")
            nombre = input("Nombre de real: ").strip()
            nombre_usuario = input("Nombre de usuario: ")
            contraseña = input("Contraseña: ").strip()
            if len(nombre_usuario) == 0 or len(contraseña) == 0 or len(nombre) == 0:
                print("Por favor rellene los campos")
                input("Presione enter para continuar")
                continue
            elif self.gestor.agregar_usuario(nombre, nombre_usuario, contraseña) == True:
                self.usuario = Usuario(nombre_usuario, contraseña)
                input("Presione enter para continuar")
                return 
            else:
                fallos += 1
                input("Presione enter para continuar")
                if fallos == 3:
                    print("Demasiados fallos, saliendo del registro")
                    break
                else:
                    continue

        

class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.__contraseña = contraseña
        self.__nombre_usuario = nombre_usuario


login = Login()

def opciones_menu_login():
    print("Bienvenido al final de Programacion 1.")
    ver_opciones = [["1. Iniciar sesion"],["2. Registrarse"],["3. Salir"]]
    print(tabulate(ver_opciones,tablefmt="fancy_grid"))

def elegir_opcion_login():
    elegir = input("Por favor ingrese el numero de la opcion deseada: ").strip()
    return elegir

def verificar_opcion(elegir):
    if elegir == "1":
        login.ingresar_usuario()
        input("Presione enter para continuar")
        
    elif elegir == "2":
        if login.registrar_usuario() == True:
            print("Inicio exitoso")      
            input("Presione enter para continuar")
        return
    elif elegir == "3":
        print("Finalizando programa...")
        input("Presione enter para continuar")
        sys.exit(0)
    else:
        print("Opcion invalida, por favor ingrese una valida")


def menu_login():
    while True:
        clear()
        opciones_menu_login()
        elegir = elegir_opcion_login()
        if verificar_opcion(elegir) == True:
            break
        else:
            continue
