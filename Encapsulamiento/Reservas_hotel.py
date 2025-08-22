import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

class Reservas_hotel:
    def __init__(self):
        self.__nombre_cliente = input("Ingrese el nombre del cliente: ")
        self.__numero_habitacion = input("Ingrese el número de habitación: ")
        self.__fecha_reserva = []
        for i in range(3):
            fecha = input(f"Ingrese la fecha de reserva {i + 1} (dd/mm/aaaa): ")
            self.__fecha_reserva.append(fecha)
    
    def modificar_nombre_cliente(self):
        while True:
            nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
            if len(nuevo_nombre) > 0 and nuevo_nombre != self.__nombre_cliente:
                self.__nombre_cliente = nuevo_nombre
                print(f"Nombre del cliente modificado a: {self.__nombre_cliente}")
                break
            else:
                print("El nombre no puede estar vacío. Intente nuevamente.")
                continue
    
    def modificar_numero_habitacion(self):
        while True:
            nuevo_numero = input("Ingrese el nuevo número de habitación: ")
            if len(nuevo_numero) > 0 and nuevo_numero != self.__numero_habitacion:
                self.__numero_habitacion = nuevo_numero
                print(f"Número de habitación modificado a: {self.__numero_habitacion}")
                break
            else:
                print("El número de habitación no puede estar vacío. Intente nuevamente.")
                continue
    
    def seleccionar_fecha_reserva(self):
        while True:
            seleccionar = input (f"seleccione la fecha de reserva a modificar (1-3): ")
            if seleccionar in ['1', '2', '3']:
                self.fecha_seleccionada = int(seleccionar) - 1
                return self.fecha_seleccionada
            else:
                print("Opción inválida. Intente nuevamente.")
                continue
    
    def modificar_fecha_reserva(self):
        self.seleccionar_fecha_reserva()
        while True:
            nueva_fecha = input("Ingrese la nueva fecha de reserva (dd/mm/aaaa): ")
            if len(nueva_fecha) > 0 and nueva_fecha != self.__fecha_reserva[self.fecha_seleccionada]:
                self.__fecha_reserva[self.fecha_seleccionada] = nueva_fecha
                print(f"Fecha de reserva modificada a: {self.__fecha_reserva}")
                break
            else:
                print("La fecha no puede estar vacía. Intente nuevamente.")
                continue
    
    def mostrar_informacion(self):
        print(f"Nombre del cliente: {self.__nombre_cliente}")
        print(f"Número de habitación: {self.__numero_habitacion}")
        print("Fechas de reserva:")
        for i, fecha in enumerate(self.__fecha_reserva):
            print(f"Fecha {i + 1}: {fecha}")
    
input("Prueba de uso")
print("creacion de la instancia y mostrando la información\n", 50 * "-")
reserva = Reservas_hotel()
reserva.mostrar_informacion()

input("Precione enter para continuar")
print("\nModificando el nombre del cliente y fecha de reserva\n", 50 * "-")
reserva.modificar_nombre_cliente()
reserva.modificar_fecha_reserva()
print("Mostrando la información actualizada\n", 50 * "-")
reserva.mostrar_informacion()