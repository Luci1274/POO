from modulos.limpiar_pantalla import clear
from modulos.vehiculos import Autos, Motocicletas

def main():
    
    while True:
        clear()
        print("Bienvenido a la concesionaria")
        print("1. Agregar Auto")
        print("2. Agregar Motocicleta")
        print("3. Ver Autos Guardados")
        print("4. ver Motocicletas Guardadas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        opciones(opcion)

def opciones(opcion):
    if opcion == '1':
        marca = input("Ingrese la marca del auto: ")
        modelo = input("Ingrese el modelo del auto: ")
        año = input("Ingrese el año del auto: ")
        precio = input("Ingrese el precio del auto: ")
        tipo_motor = input("Ingrese el tipo de motor del auto: ")
        auto = Autos(marca, modelo, año, precio, tipo_motor)
        auto.guardar_informacion()
        print("Auto guardado exitosamente.")
        input("Presione Enter para continuar...")
    elif opcion == '2':
        marca = input("Ingrese la marca de la motocicleta: ")
        modelo = input("Ingrese el modelo de la motocicleta: ")
        año = input("Ingrese el año de la motocicleta: ")
        precio = input("Ingrese el precio de la motocicleta: ")
        tipo_motor = input("Ingrese el tipo de motor de la motocicleta: ")
        moto = Motocicletas(marca, modelo, año, precio, tipo_motor)
        moto.guardar_informacion()
        print("Motocicleta guardada exitosamente.")
        input("Presione Enter para continuar...")
    elif opcion == '3':
        Autos.ver_autos_guardados()
        print("Autos guardados:")
        input("Presione Enter para continuar...")
    elif opcion == '4':
        Motocicletas.ver_motocicletas_guardadas()
        print("Motocicletas guardadas:")
        input("Presione Enter para continuar...")
    elif opcion == '5':
        print("Saliendo del programa...")
        input("Presione Enter para continuar...")
        exit()
    else:
        print("Opción no válida. Intente de nuevo.")
        input("Presione Enter para continuar...")

main()