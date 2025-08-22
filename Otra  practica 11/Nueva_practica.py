#Ejercicio: Sistema de Registro de Libros
#Requisitos:

# Crea una clase base llamada Libro con los atributos: titulo, autor y anio.
# Crea dos clases hijas:
# LibroFisico (añade el atributo ubicacion)
# LibroDigital (añade el atributo formato)
# Implementa un método en cada clase para mostrar la información del libro.
# Permite al usuario agregar libros físicos o digitales y guardarlos en un archivo CSV.
# Permite listar todos los libros guardados leyendo el archivo CSV.
# Pistas:

# Usa el módulo csv para guardar y leer los libros.
# Puedes usar una función para mostrar un menú simple en consola.

import os
import csv

def clear():
    clear = os.system("cls")
    print("-" * 50)
    return

class Libreria:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        año = input("Ingrese el año de publicación: ")
        tipo = input("Ingrese el tipo de libro (fisico/digital): ").lower()

        if tipo == "fisico":
            ubicacion = input("Ingrese la ubicación del libro físico: ")
            libro = Libro_fisico(titulo, autor, año, ubicacion)
        elif tipo == "digital":
            formato = input("Ingrese el formato del libro digital: ")
            libro = Libro_digital(titulo, autor, año, formato)
        else:
            print("Tipo de libro no válido.")
            return
        self.libros.append(libro)

    def guardar_libros(self):
        archivo_nuevo = not os.path.exists('libros.csv') or os.path.getsize('libros.csv') == 0
        with open('libros.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if archivo_nuevo:
                writer.writerow(['Titulo', 'Autor', 'Año', 'Tipo', 'Ubicacion/Formato'])
            for libro in self.libros:
                if isinstance(libro, Libro_fisico):
                    writer.writerow([libro.titulo, libro.autor, libro.año, 'Fisico', libro.ubicacion])
                elif isinstance(libro, Libro_digital):
                    writer.writerow([libro.titulo, libro.autor, libro.año, 'Digital', libro.formato])

    def listar_libros(self):
        if not os.path.exists('libros.csv'):
            print("No hay libros registrados.")
            return
        with open('libros.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                titulo, autor, año, tipo, ubicacion_formato = row
                print(f"Título: {titulo}, Autor: {autor}, Año: {año}, Tipo: {tipo}, Ubicación/Formato: {ubicacion_formato}")

class Libro:
    def __init__ (self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año


class Libro_fisico(Libro):
    def __init__ (self, titulo, autor, año, ubicacion):
        super().__init__(titulo, autor, año)
        self.ubicacion = ubicacion

class Libro_digital(Libro):
    def __init__ (self, titulo, autor, año, formato):
        super().__init__(titulo, autor, año)
        self.formato = formato
    

def menu():
    libreria = Libreria()
    while True:
        clear()
        print("Sistema de Registro de Libros")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Guardar libros")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            libreria.agregar_libro()
            input("Libro agregado correctamente. Presione Enter para continuar...")
        elif opcion == '2':
            libreria.listar_libros()
            input("Presione Enter para continuar...")
        elif opcion == '3':
            libreria.guardar_libros()
            input("Libros guardados correctamente. Presione Enter para continuar...")
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
menu()