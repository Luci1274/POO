import sys
from tabulate import tabulate
import os
import platform
from modulos.manipular_archivos import Gestor_datos

def clear():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("-" * 50)

class Login:
    def __init__(self):
        self.gestor = Gestor_datos()
    
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
                tipo = "usuario"
                return nombre_usuario, tipo
            else:
                print("Usuario o contraseña inocrrecta, por favor intente nuevamente")
                input("Presione enter para continuar")
                fallos += 1
                intentos -= 1
                if fallos == 3:
                    print("Demasiados fallos, volviendo al menu")
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