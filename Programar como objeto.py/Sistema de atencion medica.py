import random

class Medicos:
    
    def espacialidades(self):
        especialidades = {
            "1": "Medicina General",
            "2": "Pediatria",
            "3": "Ginecologia",
            "4": "Traumatologia",
            "5": "Cardiologia"
        }
        return self.espacialidades
    
    def medicos_disponibles(self):
        disponibilidad = random.choice([True, False])
        if disponibilidad == True:
            print("Hay médicos disponibles.")
            medicos = {
                "Medicina General": ["Dr. Juan Perez", "Dr. Ana Maria"],
                "Pediatria": ["Dr. Maria Lopez", "Dr. Pedro Gonzalez"],
                "Ginecologia": ["Dr. Carlos Sanchez", "Dr. Laura Gomez"],
                "Traumatologia": ["Dr. Ana Torres", "Dr. Jorge Martinez"],
                "Cardiologia": ["Dr. Luis Ramirez", "Dr. Sofia Morales"]
            }
            return self.medicos_disponibles
        else:
            print("No hay médicos disponibles en este momento.")
            input("Por favor, intente más tarde. Presione Enter para continuar.")
            exit()
    
    def seleccionar_especialidad(self):
        while True:
            print("Seleccione una especialidad:")
            for key, value in self.espacialidades().items():
                print(f"{key}. {value}")
            seleccion = input("Ingrese el número de la especialidad: ")
            if seleccion in self.espacialidades():
                return self.espacialidades()[seleccion]
            else:
                print("Opción no válida.")
    
    def seleccionar_medico(self, especialidad):
        while True:
            print(f"Seleccione un médico de {especialidad}:")
            for i, medico in enumerate(self.medicos_disponibles()[especialidad], start=1):
                print(f"{i}. {medico}")
            seleccion = input("Ingrese el número del médico: ")
            if seleccion.isdigit() and 1 <= int(seleccion) <= len(self.medicos_disponibles()[especialidad]):
                return self.medicos_disponibles()[especialidad][int(seleccion) - 1]
            else:
                print("Opción no válida.")

class Pacientes(Medicos):

    def solicitar_cita(self):
        print("Bienvenido al sistema de atención médica.")
        print("Por favor registrece antes de continuar.")
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.dni = input("Ingrese su DNI: ")
        self.telefono = input("Ingrese su número de teléfono: ")
        self.direccion = input("Ingrese su dirección: ")
        self.correo = input("Ingrese su correo electrónico: ")
        print("Registro exitoso.")
        print("Ahora puede solicitar una cita médica.")
        print("Por favor, seleccione una especialidad y un médico.")
        especialidad = self.seleccionar_especialidad()
        medico = self.seleccionar_medico(especialidad)
        print(f"Su cita ha sido programada con {medico} en la especialidad de {especialidad}.")
    
    def confirmar_cita(self):
        print("Por favor, confirme su cita médica.")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")
        print(f"Correo: {self.correo}")
        print("¿Desea confirmar la cita? (s/n)")
        confirmacion = input()
        if confirmacion.lower() == "s":
            print("Cita confirmada.")
        else:
            print("Cita cancelada.")
            exit()

    def recordatorio_cita(self):
        # Se envia un recordatorio al paciente a travez del correo electronico
        print("Recordatorio de cita médica.")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")
        print("Recuerde asistir a su cita médica.")    
