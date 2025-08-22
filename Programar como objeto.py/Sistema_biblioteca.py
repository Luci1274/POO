import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

import random

class sistema:

    def mostrar_catalogo(self):
        catalogo = ["El principito", "Cien años de soledad", "Crónica de una muerte anunciada", "Rayuela", "El túnel"]
        for libro in catalogo:
            print(f"Libro: {libro}")
        return catalogo
    
    def disponibilidad (self):
        disponibilidad = random.choice([True, False])
        while True:
            if disponibilidad == True:
                print("El libro está disponible")
                break
            else:
                clear()
                print("El libro no está disponible")
                input("Precione enter para continuar")
                while True:
                    print("Desea recibir una notificación cuando el libro esté disponible? (si/no)")
                    respuesta = input()
                    if respuesta.lower() == "si":
                        print("Se le notificará cuando el libro esté disponible")
                        input("Precione enter para continuar")
                        clear()
                        self.mostrar_catalogo()
                        break
                    elif respuesta.lower() == "no":
                        clear()
                        print("No se le notificará cuando el libro esté disponible")
                        input("Precione enter para continuar")
                        exit()
                    else:
                        clear()
                        print("Respuesta no válida, por favor intente de nuevo")
                        input("Precione enter para continuar")
                        continue
        return disponibilidad
    
    def entregar_libro(self):
        print("El libro ha sido entregado")

class CLiente(sistema):
    
    def selecionar_libro(self):
        print("Seleccione el libro que desea llevarse")
        self.catalogo = self.mostrar_catalogo()
        while True:
            self.libro_elegido = input("Ingrese el número del libro que desea llevarse: ")
            if self.libro_elegido in self.catalogo:
                print(f"Usted ha elegido el libro: {self.libro_elegido}")
                self.disponibilidad = self.disponibilidad()
                return self.libro_elegido
            else:
                print("El libro no está en el catálogo, por favor intente de nuevo")
                continue
    
    def realizar_reserva(self):
        clear()
        print("Realizando reserva...")
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.correo = input("Ingrese su correo: ")
        self.telefono = input("Ingrese su teléfono: ")
        self.DNI = input("Ingrese su DNI: ")
        print(f"Libro elegido {self.libro_elegido}")
        self.entregar_libro()

cliente = CLiente()
cliente.selecionar_libro()
cliente.realizar_reserva()