from clear import clear
from apis.dog_api import dog_api, abrir_buscador
from apis.joke_api import obtener_chiste, traducir_texto
from apis.dolar_api import Dolar_oficial, Dolar_tarjeta, Dolar_blue

def mostrar_opciones():
    print("Bienvenido a pruebas api, Por favor vea las opciones")
    print("1. Fotos de perros\n","2. chistes\n","3. Dolar\n" ,"4. cerrar sesion")

def elegir_opcion():
    opcion = input("Ingrese la opcion deseada: ")
    return opcion

def verificar_opcion(opcion):
    while True:
        if opcion == "1":
            image_url = dog_api()
            abrir_imagen(image_url)
            input("Presione enter para continuar")
            break
        
        elif opcion == "2":
            traducir_chiste()
            input("Presione enter para continuar")
            break
        
        elif opcion == "3":
            menu_dolar()
            break

        elif opcion == "4":
            print("Gracias por participar en esta prueba")
            exit()
        
        else:
            print("Opcion incorrecta intente nuevamente")
            input("Presione enter para continuar")

def abrir_imagen(image_url):
    print("Desea abrir la imagen en el buscador? S/N")
    opcion = input("").strip().upper()
    if opcion == "S":
        abrir_buscador(image_url)
    else:
        print("Ah decidido no hacerlo")

def traducir_chiste():
    clear()
    print("Desea traducir el chiste? S/N")
    respuesta = input("").strip().upper()
    if respuesta == "S":
        chiste = obtener_chiste()
        print(chiste)
    elif respuesta == "N":
        chiste = obtener_chiste()
        traduccion = traducir_texto(chiste, origen="en", destino="es")
        print("\nChiste traducido al español:")
        print(traduccion)
    else:
        print("Opcion incorrecta")
        input("Presione enter para continuar")

def menu():
    while True:
        clear()
        mostrar_opciones()
        opcion = elegir_opcion()
        verificar_opcion(opcion)

def menu_dolar():
    clear()
    mostrar_opciones_dolar()
    opcion_dolar = elegir_opcion_dolar()
    verificar_opcion_dolar(opcion_dolar)
    return

def mostrar_opciones_dolar():
    print("Ingrese una de estas opciones: ")
    print("1. Dolar oficial\n","2. Dolar tarjeta\n","3. Dolar Blue\n" ,"4. salir")

def elegir_opcion_dolar():
    opcion_dolar = input("Ingrese el numero de una de las opcines: ")
    return opcion_dolar

def verificar_opcion_dolar(opcion_dolar):
    while True:
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

menu()