import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

class Sistema:

    def registrar_votante(self):
        # Aquí se implementaría la lógica para registrar un votante
        Nombre = input("Ingrese el nombre del votante: ")
        Apellido = input("Ingrese el apellido del votante: ")
        DNI = input("Ingrese el DNI del votante: ")
        datos_votante = {"Nombre": Nombre, "Apellido": Apellido, "DNI": DNI}
        return datos_votante

    def mostrar_opciones(self):
        opciones = {"opcion A": "candidato jose",
                    "opcion B": "candidato juan",
                    "opcion C": "candidato pedro",
                    "opcion D": "candidato pablo"}
        return opciones

    def confirmar_voto(self):
        # Aquí se implementaría la lógica para confirmar el voto
        while True:
            confirmacion = input("¿Está seguro de su voto? (si/no): ").lower()
            if confirmacion == "si":
                print("Voto confirmado")
                break
            elif confirmacion == "no":
                print("Volviendo a las opciones de voto...")
                input("Presione Enter para continuar...")
                self.mostrar_opciones
                self.votar()
                break
            else:
                print("Opción no válida. Intente nuevamente.")
                input("Presione Enter para continuar...")
                self.mostrar_opciones
                self.votar()
                break
                continue

class Votante(Sistema):
    
    def __init__ (self):
        self.datos_votante = self.registrar_votante()
        self.opciones = self.mostrar_opciones()
    
    def votar(self):
        print("Opciones de voto:")
        for key, value in self.opciones.items():
            print(f"{key}: {value}")
        
        voto = input("Ingrese su opción de voto: ")
        while True:
            if voto in self.opciones:
                print(f"Usted ha votado por: {self.opciones[voto]}")
                self.confirmar_voto()
                break
            else:
                print("Opción no válida. Intente nuevamente.")
                continue

votante = Votante()
votante.votar()