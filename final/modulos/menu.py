import os
import platform
from modulos.apis.dog_api import abrir_imagen
from modulos.apis.joke_api import traducir_chiste
from modulos.apis.dolar_api import Dolar_oficial, Dolar_tarjeta, Dolar_blue
from tabulate import tabulate

def clear():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print("-" * 50)

def mostrar_opciones():
    print("Bienvenido a pruebas api, Por favor vea las opciones")
    ver_opciones_menu = [["1. Fotos de perros"],["2. chistes"],["3. Dolar"] ,["4. cerrar sesion"]]
    print(tabulate(ver_opciones_menu,tablefmt="fancy_grid"))
    return ver_opciones_menu

def elegir_opcion():
    opcion = input("Ingrese la opcion deseada: ")
    return opcion

def verificar_opcion(opcion):
    clear()
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
        menu_dolar()
        ultima_pagina_visitada = "Api dolar"
        return ultima_pagina_visitada
    elif opcion == "4":
        print("Gracias por participar en esta prueba")
        return None
    else:
        print("Opcion incorrecta intente nuevamente")
        input("Presione enter para continuar")
        return True

def menu():
    nuevo_ingreso = 1
    paginas_visitadas = 0
    paginas = []
    while True:
        clear()
        ver_opciones_menu = mostrar_opciones()
        opcion = elegir_opcion()
        pagina = verificar_opcion(opcion)
        paginas.append(pagina)
        if  len(paginas) == 1 and paginas[0] == None:
            ultima_pagina_visitada = paginas[0]
            return nuevo_ingreso, paginas_visitadas, ultima_pagina_visitada
        elif len(paginas) != 1 and paginas[-1] == None:
            ultima_pagina_visitada = paginas[-2]
            return nuevo_ingreso, paginas_visitadas, ultima_pagina_visitada
        else:
            paginas_visitadas += 1
            continue

def menu_dolar():
    clear()
    mostrar_opciones_dolar()
    opcion_dolar = elegir_opcion_dolar()
    verificar_opcion_dolar(opcion_dolar)
    return

def mostrar_opciones_dolar():
    print("Ingrese una de estas opciones: ")
    ver_opciones_dolar = [["1. Dolar oficial"],["2. Dolar tarjeta"],["3. Dolar Blue"] ,["4. Regresar"]]
    print(tabulate(ver_opciones_dolar,tablefmt="fancy_grid"))

def elegir_opcion_dolar():
    opcion_dolar = input("Ingrese el numero de una de las opcines: ")
    return opcion_dolar

def verificar_opcion_dolar(opcion_dolar):
    while True:
        clear()
        if opcion_dolar == "1":
            dolar_oficial = Dolar_oficial()
            dolar_oficial.mostrar_info()
            input("Presione enter para continuar")
            break
        
        elif opcion_dolar == "2":
            dolar_tarjeta = Dolar_tarjeta()
            dolar_tarjeta.mostrar_info()
            input("Presione enter para continuar")
            break
        
        elif opcion_dolar == "3":
            dolar_blue = Dolar_blue()
            dolar_blue.mostrar_info()
            input("Presione enter para continuar")
            break

        elif opcion_dolar == "4":
            print("Regresando al menu principal")
            break
        
        else:
            print("Opcion incorrecta intente nuevamente")
            input("Presione enter para continuar")
