import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

import random

class Soporte_tecnico:

    def recibir_solicitud(self):
        print("Recibiendo solicitud de soporte técnico...")
        # Aquí puedes agregar la lógica para recibir la solicitud
        print("Solicitud recibida.")
        print("Por favor, proporcione la siguiente información:")
        nombre_cliente = input("Nombre del cliente: ")
        problema = input("Descripción del problema: ")
        nombre_equipo = input("Escriba el nombre del equipo: ")
        marca_equipo = input("Escriba la marca del equipo: ")
        print("Solicitud de soporte técnico recibida.")
        print(f"Cliente: {nombre_cliente}")
        print(f"Nombre del {nombre_equipo}, marca {marca_equipo}")
        print(f"Problema: {problema}")
        datos = [nombre_cliente, nombre_equipo, marca_equipo, problema]
        return datos
    
    def asignar_tecnico(self, datos):
        print(f"Asignando técnico al cliente {datos[0]}...")
        # Aquí puedes agregar la lógica para asignar un técnico
        tecnico = "Técnico 1"
        print(f"Técnico asignado: {tecnico}")
        return tecnico
    
    def diagnosticar_problema(self, datos):
        print(f"Diagnosticando el problema: {datos[3]}...")
        # Aquí puedes agregar la lógica para diagnosticar el problema
        solucion = random.choice([True, False])
        soluciones = {"1": "reiniciar", "2": "borrar archivo ....", "3": "formatear"}
        if solucion == True:
            print("Diagnóstico completo. Solución recomendadas:")
            for key, value in soluciones.items():
                print(f"{key}, {value}")
        else:
            clear()
            print("Su problema no tiene una solución lo sentimos mucho")
            exit()
        return soluciones

class Cliente(Soporte_tecnico):
    def __init__(self):
        self.datos = self.recibir_solicitud()
        self.tecnico = self.asignar_tecnico(self.datos)
        self.solucion = self.diagnosticar_problema(self.datos)
    
    def rearlizar_solucion(self):
        print("Desea realizar la solución?")
        while True:
            respuesta = input("Escriba 'si' o 'no': ").lower()
            if respuesta == "si":
                print("Realizando solución...")
                # Aquí puedes agregar la lógica para realizar la solución
                print("Solución realizada.")
                break
            elif respuesta == "no":
                print("No se realizará la solución.")
                exit()
                break
            else:
                print("Respuesta no válida. Intente nuevamente.")

cliente = Cliente()
cliente.rearlizar_solucion()
