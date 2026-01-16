import sys
import os
import platform
from tabulate import tabulate
from modulos.login import Login
from modulos.apis.img_api import Dog_api, Cat_api
from modulos.apis.joke_api import traducir_chiste
from modulos.apis.dolar_api import Dolar_oficial, Dolar_tarjeta, Dolar_blue, Dolar_cripto
from modulos.apis.freetogame_api import Free_to_game_api
from time import sleep
from modulos.manipular_archivos import Gestor_datos

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
        clear()
    
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
            clear()
            self.opciones_menu()
            elegir = self.elegir_opcion()
            resultado = self.verificacion_opcion()
            
class Menu_login(Menu_base):
    def __init__(self):
        clear()
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
        clear()
        self.dog = Dog_api()
        self.cat = Cat_api()
        self.traducir_chiste = traducir_chiste
        self.menu_dolar = Menu_dolar()
        self.menu_free_to_game = Menu_free_to_game()
    
    def opciones_menu(self):
        print("Bienvenido a pruebas api, Por favor vea las opciones")
        ver_opciones_menu = [["1. Fotos de perros"], ["2. Fotos de gatos"], ["3. chistes"], ["4. Dolar"], ["5. información de juegos"]]
        ver_opciones_menu.append([str(len(ver_opciones_menu) + 1) + ". Para borrar la cuenta"])
        ver_opciones_menu.append([str(len(ver_opciones_menu) + 1) + ". Para salir"])
        print(tabulate(ver_opciones_menu,tablefmt="fancy_grid"))
        return ver_opciones_menu
    
    def verificar_opcion(self, opcion, ver_opciones_menu):
        clear()
        if opcion == "1":
            self.dog.abrir_imagen()
            input("Presione enter para continuar")
            ultima_api_visitada = "Api perros"
            return ultima_api_visitada
        
        elif opcion == "2":
            self.cat.abrir_imagen()
            input("Presione enter para continuar")
            ultima_api_visitada = "Api gatos"
            return ultima_api_visitada
        
        elif opcion == "3":
            self.traducir_chiste()
            input("Presione enter para continuar") 
            ultima_api_visitada = "Api chistes"
            return ultima_api_visitada   
        
        elif opcion == "4":
            ultima_api_visitada = self.menu_dolar.ejecutar()
            return ultima_api_visitada
        
        elif opcion == "5":
            ultima_api_visitada = self.menu_free_to_game.ejecutar()
            return ultima_api_visitada
        
        elif opcion == str(len(ver_opciones_menu) - 1):
            verificar = input("Presione borrar cuenta ¿Está seguro? S/N: ").strip().upper()
            if verificar == "S" or verificar == "SI" or verificar == "YES":
                return "Eliminar"
            else:
                return "Error"
                
        elif opcion == str(len(ver_opciones_menu)):
            print("Gracias por participar en esta prueba")
            return "Salir"
        else:
            print("Opcion incorrecta intente nuevamente")
            input("Presione enter para continuar")
            return "Error"
    
    def ejecutar(self):
        nuevo_ingreso = 1
        apis_visitadas = 0
        apis = []
        consultas_api = {}
        while True:
            clear()
            ver_opciones_menu = self.opciones_menu()
            opcion = self.elegir_opcion()
            api = self.verificar_opcion(opcion, ver_opciones_menu)
            apis.append(api)
            """
            Guardar las consultas de las apis
            """
            if api not in ["Salir", "Error", "Eliminar"]:
                consultas_api[api] = consultas_api.get(api, 0) + 1
            """
            Salir del menu al login
            """
            if  len(apis) == 1 and apis[0] == "Salir":
                ultima_api_visitada = "ninguna"
                
                return nuevo_ingreso, apis_visitadas, ultima_api_visitada, False, consultas_api
            elif len(apis) == 1 and apis[0] == "Eliminar":
                ultima_api_visitada = "ninguna"
                return nuevo_ingreso, apis_visitadas, ultima_api_visitada, True, consultas_api
            elif len(apis) > 1 and apis[-1] == "Salir":
                ultima_api_visitada = apis[-2]
                return nuevo_ingreso, apis_visitadas, ultima_api_visitada, False, consultas_api
            elif len(apis) > 1 and apis[-1] == "Eliminar" and apis[-2] != "Error":
                ultima_api_visitada = apis[-2]
                return nuevo_ingreso, apis_visitadas, ultima_api_visitada, True, consultas_api
            else:
                apis_visitadas += 1
                continue

class Menu_dolar(Menu_base):
    def __init__(self):
        clear()
        self.Dolar_oficial = Dolar_oficial
        self.Dolar_tarjeta = Dolar_tarjeta
        self.Dolar_blue = Dolar_blue
    
    def opciones_menu(self):
        print("Ingrese una de estas opciones: ")
        ver_opciones_dolar = [["1. Dolar oficial"],["2. Dolar tarjeta"],["3. Dolar Blue"], ["4. Dolar cripto"]]
        ver_opciones_dolar.append([str(len(ver_opciones_dolar) + 1) + ". regresar"])
        print(tabulate(ver_opciones_dolar,tablefmt="fancy_grid"))
        return ver_opciones_dolar
    
    def verificar_opcion(self, opcion, ver_opciones_dolar):
        while True:
            clear()
            if opcion == "1":
                dolar_oficial = Dolar_oficial()
                dolar_oficial.mostrar_info()
                input("Presione enter para continuar")
                return "Dolar oficial"
            
            elif opcion == "2":
                dolar_tarjeta = Dolar_tarjeta()
                dolar_tarjeta.mostrar_info()
                input("Presione enter para continuar")
                return "Dolar tarjeta"
            
            elif opcion == "3":
                dolar_blue = Dolar_blue()
                dolar_blue.mostrar_info()
                input("Presione enter para continuar")
                return "Dolar blue"
            
            elif opcion == "4":
                dolar_cripto = Dolar_cripto()
                dolar_cripto.mostrar_info()
                input("Presione enter para continuar")
                return "Dolar cripto"

            elif opcion == str(len(ver_opciones_dolar)):
                print("Regresando al menu principal")
                return "Ninguno"
            
            else:
                print("Opcion incorrecta intente nuevamente")
                input("Presione enter para continuar")
                break

    def ejecutar(self):
        clear()
        ver_opciones_dolar = self.opciones_menu()
        opcion = self.elegir_opcion()
        api_dolar_visitada = self.verificar_opcion(opcion, ver_opciones_dolar)
        return api_dolar_visitada
    
class Menu_free_to_game(Menu_base):
    def __init__(self):
        clear()
        self.freetogame = Free_to_game_api()
    
    def opciones_menu(self):
        ver_opciones_menu = [["1. Mostrar cantidad  juegos a eleccion"], ["2. Buscar juego por ID"]]
        ver_opciones_menu.append([str(len(ver_opciones_menu) + 1) + ". Para salir"])
        print(tabulate(ver_opciones_menu,tablefmt="fancy_grid"))
        return ver_opciones_menu
    
    def verificar_opcion(self, opcion, ver_opciones_menu):
        clear()
        if opcion == "1":
            juegos_totales = self.freetogame.contar_juegos()
            if juegos_totales == 0 or None:
                input("Presione enter para continuar")
                return
            else:
                print(f"La cantidad de IDs es de: {juegos_totales}\n")
            try:
                cantidad = int(input("Ingrese la cantidad de juegos a buscar: ").strip())
                if cantidad >= 1 and cantidad <= juegos_totales:
                    self.freetogame.obtener_todos(cantidad)
                    input("Presione enter para continuar")
                    return
                else:
                    print("El numero debe de ser mayor a 0")
                    input("Presione enter para continuar") 
                    return   
            except:
                print("Se debe de ingresar un numero")
                input("Presione enter para continuar")
                return
                    
        elif opcion == "2":
            clear()
            juegos_totales = self.freetogame.contar_juegos()
            if juegos_totales == 0 or None:
                print("Presione enter para continuar")
                return
            else:
                print(f"La cantidad de IDs es de: {juegos_totales}\n")
            try:
                ID = int(input("Ingrese un ID: ").strip())
                if ID >= 1 and ID <= juegos_totales:
                    self.freetogame.obtener_por_id(ID)
                    input("Presione enter para continuar")
                    return
                else:
                    print(f"El ID debe de ser mayor a 0 y menor a {juegos_totales}")
                    input("Presione enter para continuar")
                    return
            except:
                print("Se debe de ingresar un numero")
                input("Presione enter para continuar")
                return

        else:
            print("Opcion incorrecta intente nuevamente")
            input("Presione enter para continuar")
            return
            
            
    def ejecutar(self):
        clear()
        ver_opciones_menu = self.opciones_menu()
        opcion = self.elegir_opcion()
        if opcion == str(len(ver_opciones_menu)):
            return "Free to Games Api"
        else:
            self.verificar_opcion(opcion, ver_opciones_menu)

class Menu_administrador(Menu_base):
    def __init__(self):
        clear()
        self.gestor_datos = Gestor_datos()
    
    def opciones_menu(self):
        ver_opciones_menu = [["1. Ver datos usuarios activos/inactivos"], ["2. Ver datos usuarios activos"], ["3. Ver datis usuarios inanctivos"], ["4. Ver consultas apis"]]
        
        ver_opciones_menu.append([str(len(ver_opciones_menu) + 1) + ". Agregar administrador"])
        ver_opciones_menu.append([str(len(ver_opciones_menu) + 1) + ". Para salir"])
        print(tabulate(ver_opciones_menu,tablefmt="fancy_grid"))
        return ver_opciones_menu

    def verificar_opcion(self, opcion, ver_opciones_menu):
        clear()
        if opcion == "1":
            datos_tabla = self.gestor_datos.obtener_datos_usuarios()
            print(tabulate(datos_tabla, headers=["Nombre", "Usuario", "Ingresos", "Páginas Visitadas", "Última Página"], tablefmt="fancy_grid"))
            input("Presione enter para continuar")
        
        elif opcion == "2":
            datos_tabla = self.gestor_datos.obtener_datos_usuarios_activos()
            print(tabulate(datos_tabla, headers=["Nombre", "Usuario", "Ingresos", "Páginas Visitadas", "Última Página"], tablefmt="fancy_grid"))
            input("Presione enter para continuar")
        
        elif opcion == "3":
            datos_tabla = self.gestor_datos.obtener_datos_usuarios_inactivos()
            print(tabulate(datos_tabla, headers=["Nombre", "Usuario", "Ingresos", "Páginas Visitadas", "Última Página"], tablefmt="fancy_grid"))
            input("Presione enter para continuar")
        
        elif opcion == "4":
            datos_tabla = self.gestor_datos.obtener_consultas_apis()
            print(tabulate(datos_tabla, headers=["Nombre Api", "Veces consultadas"], tablefmt="fancy_grid"))
            input("Presione enter para continuar")
        
        elif opcion == str(len(ver_opciones_menu)- 1):
            nombre = input("Ingrese el nombre del nuevo ad: ")
            contraseña = input("Ingrese la contraseña: ")
            self.gestor_datos.agregar_administrador(nombre, contraseña)
            input("Presione enter para continuar")   
        else:
            print("ENSERIO? HOMBRE ERES ADMINISTRADOR!!!!")
            input("Presione enter para continuar")
            
    def ejecutar(self):
        while True:
            clear()
            ver_opciones_menu = self.opciones_menu()
            opcion = self.elegir_opcion()
            if opcion == str(len(ver_opciones_menu)):
                break
            else:
                self.verificar_opcion(opcion, ver_opciones_menu)