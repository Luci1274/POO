import os
import platform
from tabulate import tabulate
from modulos.manipular_archivos import Gestor_datos

gestor_datos = Gestor_datos()

def clear():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print("-" * 50)
    
def ver_opciones_menu():
    opciones_menu = [["1. Ver datos usuarios"], ["2. Agregar administrador"], ["3. Filtrar datos"], ["4. Volver al menu"]]
    print(tabulate(opciones_menu,tablefmt="fancy_grid"))

def elegir_opcion_menu():
    opcion = input("Ingrese la opcion deseada: ").strip()
    return opcion

def validar_opcion_menu(opcion):
    clear()
    if opcion == "1":
        datos_tabla = gestor_datos.obtener_datos_usuarios()
        print(tabulate(datos_tabla, headers=["Nombre", "Usuario", "Ingresos", "Páginas Visitadas", "Última Página"], tablefmt="fancy_grid"))
        input("Presione enter para continuar")
        
    elif opcion == "2":
        nombre = input("Ingrese el nombre del nuevo ad: ")
        contraseña = input("Ingrese la contraseña: ")
        gestor_datos.agregar_administrador(nombre, contraseña)
        input("Presione enter para continuar") 
    
    elif opcion == "3":
        menu_filtrado()
        input("Presione enter para continuar")
            
    else:
        print("ENSERIO? HOMBRE ERES ADMINISTRADOR!!!!")
        input("Presione enter para continuar")
        
def menu_filtrado():
    clave = elegir_clave()
    valor = elegir_valor(clave)
    filtrados = gestor_datos.filtrar_datos_varios(clave, valor) 
    print(tabulate(filtrados,headers=["nombre", "nombre_usuario", "veces ingresadas", "cantidad_paginas_visitadas", "ultima_pagina_visitada"], tablefmt="fancy_grid"))    

def elegir_clave():
    mostrar_claves = [["nombre"], ["nombre_usuario"], ["veces ingresadas"], ["cantidad_paginas_visitadas"], ["ultima_pagina_visitada"]]
    print(tabulate(mostrar_claves,tablefmt="fancy_grid"))
    clave = input("Ingrese la clave por la cual filtrar:")
    return clave

def elegir_valor(clave):
    valores = gestor_datos.mostrar_valores(clave)
    print(tabulate(valores,tablefmt="fancy_grid"))
    print("Escriba el valor por el cual filtrar")
    valor = input("Ingrese el valor").lower().strip()
    return valor
    
    

def menu_administrador():
    while True:
        clear()
        ver_opciones_menu()
        opcion = elegir_opcion_menu()
        if opcion == "4":
            break
        else:
            validar_opcion_menu(opcion)