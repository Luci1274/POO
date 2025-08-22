import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

class Proceso_de_inscripcion:

    def formulario(self):
        while True:
            print("Formulario de inscripción")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            correo = input("Correo electrónico: ")
            telefono = input("Teléfono: ")
            datos = {
                "nombre": nombre,
                "edad": edad,
                "correo": correo,
                "telefono": telefono
            }
            print("¿El formulario está completo?")
            pregunta = input("Sí/No: ")
            if pregunta.lower() == "sí" or pregunta.lower() == "si":
                print("Formulario completado con éxito")
                
                return  datos
            else:
                print("Vuelva a completar los datos")
    
    def recibir_documentos(self):
        print("Debe enviar los siguientes documentos:")
        print("1. Copia de la cédula de identidad")
        print("2. Titulo secundario")
        print("3. Carnet de salud")
        print("4. Certificado de buena conducta")
        print("5. 2 fotos tamaño carnet")

class Estudiante(Proceso_de_inscripcion):
    
    def enviar_documentos(self):
        print("Enviando documentos...")
        print("Documentos enviados con éxito")
        documentos = {
            "copia_cedula": "Copia de la cédula de identidad",
            "titulo_secundario": "Titulo secundario",
            "carnet_salud": "Carnet de salud",
            "certificado_buena_conducta": "Certificado de buena conducta",
            "fotos": "2 fotos tamaño carnet"
        }
        return documentos

    def __init__(self):
        self.datos = self.formulario()
        precione = input("Presione Enter para continuar...")
        clear()
        print("Desea enviar los documentos requeridos?")
        pregunta = input("Sí/No: ")
        clear()
        if pregunta.lower() == "sí" or pregunta.lower() == "si":
            self.documentos = self.enviar_documentos()
            self.recibir_documentos()
            print("Inscripción completada con éxito")
            precione = input("Presione Enter para continuar...")
            clear()
            print("Datos del estudiante:")
            for key, value in self.datos.items():
                print(f"{key}: {value}")
            print("Documentos enviados:")
            for key, value in self.documentos.items():
                print(f"{key}: {value}")
            print("Inscripción completada con éxito")
        else:
            print("No se enviaron los documentos requeridos")
            exit()

estudiante = Estudiante()
        

        
    
