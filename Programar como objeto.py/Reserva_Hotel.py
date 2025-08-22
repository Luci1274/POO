import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Habitación:
    
    def listado_habitaciones(self):
        print("Lista de habitaciones disponibles:")
        habitaciones = ["Habitación sencilla", "Habitación doble", "Suite"]
        #se puede agregar una lista de habitaciones con numero de cada habitacion junto a su tipo
        print(f"- {habitaciones}")
        return
    
    def filtar_habitaciones(self):
        print("¿Por que tipo de estado desea filtar? Disponible o No disponible")
        while True:
            estado = input()
            estado = estado.lower()
            disponibles = {"sencilla": [100, 103, 105], "doble": [110, 113, 114], "suite": [201,202]}
            no_disponibles = {"habitación_sencilla": [101, 102], 
                            "habitación_doble": [111], 
                            "suite": [203, 204]}
            if estado != "disponible" and estado != "no disponible":
                print("Estado no válido. Seleccione 'disponible' o 'no disponible'.")
            elif estado == "disponible":
                print("Habitaciones disponibles:")
                print(f"{disponibles}")
                return disponibles
            else:
                print("Habitaciones no disponibles:")
                print(f"{no_disponibles}")
                print("¿Desea ver las habitaciones disponibles? (si/no)")
                while True:
                    respuesta = input()
                    respuesta = respuesta.lower()
                    if respuesta != "si" and respuesta != "no":
                        print("Respuesta no válida. Seleccione 'si' o 'no'.")
                    elif respuesta == "si":
                        self.filtar_habitaciones(disponibles)
                        return
                    else:
                        print("Saliendo del filtro de habitaciones.")
                        exit()
    
    def seleccionar_habitacion(self, disponibles):
        clear()
        print("¿Qué tipo de habitación desea reservar? sencilla, doble o suite?")
        while True:
            print(f"habitaciones disponibles: {disponibles}")
            tipo_de_habitacion = input()
            if tipo_de_habitacion not in disponibles:
                print("tipo de habitación no disponible. Seleccione un tipo de habitación de la lista.")
                input("Presione Enter para continuar...")
                clear()
            else:
                print(f"Has seleccionado {disponibles[tipo_de_habitacion]}.")
                break
        print("¿Qué numero de habitación desea?")
        while True:
            numero_de_habitacion = input()
            numero_de_habitacion = int(numero_de_habitacion)
            if not numero_de_habitacion in disponibles[tipo_de_habitacion]:
                print("Habitación no disponible. Seleccione una habitación de la lista.")
            else:
                print(f"Has seleccionado la Habitación: {numero_de_habitacion}, del tipo: {tipo_de_habitacion}.")
                return tipo_de_habitacion,numero_de_habitacion
        
class reserva(Habitación):
    
    def __init__(self):
        self.listado_habitaciones()
        clear()
        self.tipo_de_habitacion, self.numero_de_habitacion = self.seleccionar_habitacion(self.filtar_habitaciones())
        
    def confirmar_reserva(self):
        clear()
        print("¿Desea confirmar la reserva? (si/no)")
        while True:
            confirmacion = input()
            confirmacion = confirmacion.lower()
            if confirmacion != "si" and confirmacion != "no":
                print("Respuesta no válida. Seleccione 'si' o 'no'.")
            elif confirmacion == "si":
                print("Reserva confirmada.")
                break
            else:
                print("Reserva cancelada.")
                break
    
    def ingresar_datos(self):
        print("Ingrese su nombre:")
        self.nombre = input()
        print("Ingrese su apellido:")
        self.apellido = input()
        print("Ingrese su número de documento:")
        self.documento = input()
        print("Ingrese su fecha de nacimiento (DD/MM/AAAA):")
        self.fecha_nacimiento = input()
        print("Ingrese su número de teléfono:")
        self.telefono = input()
        print("Ingrese su correo electrónico:")
        self.correo = input()
        print(f"Reserva a nombre de {self.nombre} {self.apellido}.")
        print(f"Su numero de documento es: {self.documento}.")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}.")
        print(f"Teléfono: {self.telefono}.")
        print(f"Correo electrónico: {self.correo}.")

    def mostrar_reserva(self):
        clear()
        print(f"Detalles de la reserva enviados al mail: {self.correo}")
        #esta funcion simula el envio de un correo electronico con toda la informacion de la reserva
        print(f"Tipo de habitación: {self.tipo_de_habitacion}")
        print(f"Número de habitación: {self.numero_de_habitacion}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Documento: {self.documento}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo electrónico: {self.correo}")

pedro = reserva()
pedro.ingresar_datos()
pedro.confirmar_reserva()
pedro.mostrar_reserva()