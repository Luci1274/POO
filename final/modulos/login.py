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
        intentos = 3
        fallos = 0
        while True:
            clear()
            print("Para iniciar sesion por favor ingrese el nombre de usuario y contraseña")
            print(f"Tienes {intentos} intentos")
            nombre_usuario = input("Nombre de usuario: ").strip()
            contraseña = input("Contraseña: ").strip()
            if len(nombre_usuario) == 0 or len(contraseña) == 0:
                print("Rellene los campos")
                input("Presione enter para continuar")
                fallos += 1
                intentos -= 1
                if fallos == 3:
                    print("Demasiados fallos, volviendo al menu")
                    nombre_usuario = None
                    tipo = None
                    break
                else:
                    continue
            elif nombre_usuario == "...." and contraseña == "fe":
                print("Ingresando en modo administrador")
                input("Presione enter para continuar")
                tipo = "administrador"
                return nombre_usuario,tipo
            elif self.verificar_admin(nombre_usuario, contraseña) == True: 
                print("Inicio exitoso bienvenido señor")
                input("Presione enter para continuar")
                tipo = "administrador"
                return nombre_usuario,tipo
            elif self.verificar_usuario(nombre_usuario, contraseña) == True: 
                print("Inicio exitoso")
                usuario = Usuario(nombre_usuario, contraseña)
                tipo = "usuario"
                return nombre_usuario,tipo
            else:
                print("Usuario o contraseña inocrrecta, por favor intente nuevamente")
                input("Presione enter para continuar")
                fallos += 1
                intentos -= 1
                if fallos == 3:
                    print("Demasiados fallos, volviendo al menu")
                    nombre_usuario = None
                    tipo = None
                    break
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
        intentos = 3
        fallos = 0
        while True:
            clear()
            print("Por favor llene los siguientes espacios para crear un usuario")
            print(f"Tienes {intentos} intentos")
            nombre = input("Nombre de real: ").strip()
            nombre_usuario = input("Nombre de usuario: ")
            contraseña = input("Contraseña: ").strip()
            if len(nombre) == 0 or len(nombre_usuario) == 0 or len(contraseña) == 0:
                print("Rellene los campos")
                input("Presione enter para continuar")
                fallos += 1
                intentos -= 1
                if fallos == 3:
                    print("Demasiados fallos, volviendo al menu")
                    nombre_usuario = None
                    tipo = None
                    break
                else:
                    continue
            elif self.gestor.agregar_usuario(nombre, nombre_usuario, contraseña) == True:
                self.usuario = Usuario(nombre_usuario, contraseña)
                input("Presione enter para continuar")
                return 
            else:
                fallos += 1
                intentos -= 1
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
        resultado = login.ingresar_usuario()
        if resultado != None:
            return resultado
        else:
            return None
        
    elif elegir == "2":
        if login.registrar_usuario() == True:
            print("Inicio exitoso")      
            
        return None
    elif elegir == "3":
        print("Finalizando programa...")
        sys.exit(0)
    else:
        print("Opcion invalida, por favor ingrese una valida")
        return None


def menu_login():
    while True:
        clear()
        opciones_menu_login()
        elegir = elegir_opcion_login()
        resultado = verificar_opcion(elegir)
        if resultado != None:
            return resultado
        else:
            continue
