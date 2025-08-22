# Clases
# °Examenes
# °Login
# °Profesores
# °Alumnos

# pseudo_codigo
# Inicio:
# °Login
# °Crear examen si es profesor
# ° Elegir tipo
# ° Ingresar consignas
# °Realiar examen si es alumno
# ° Devolver nota


import os

def clear():
    try:
        os.system("cls")
        os.system("clear")
        clear = print("-" * 50)
    except:
        pass
class Login:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def crear_archivos(self):
        try:
            self.archivo_profesores = open("Practicas de POO/Simulacion/Archivos/Profesores.csv", "x")
            self.archivo_alumnos = open("Practicas de POO/Simulacion/Archivos/Alumnos.csv", "x")
            self.archivo_profesores.close()
            self.archivo_alumnos.close()
        except:
            pass
    
    def abrir_archivo_modo_lectura(self):
        self.archivo_alumnos = open("Practicas de POO/Simulacion/Archivos/Alumnos.csv", "r")
        self.archivo_profesores = open("Practicas de POO/Simulacion/Archivos/Profesores.csv", "r")
    
    def abrir_archivo_modo_añadir(self):
        self.archivo_alumnos = open("Practicas de POO/Simulacion/Archivos/Alumnos.csv", "a")
        self.archivo_profesores = open("Practicas de POO/Simulacion/Archivos/Profesores.csv", "a")

    def guardar_usuario(self):
        while True:
            clear()
            print("Usuario no encontrado.\n indique a que clase pertenece: Profesor, Alumno")
            elegir = input("").lower().strip()
            self.abrir_archivo_modo_añadir()
            if elegir == "profesor":
                self.archivo_profesores.write(self.nombre + "," + self.apellido + "\n")
                return
            elif elegir == "alumno":
                self.archivo_alumnos.write(self.nombre + "," + self.apellido + "\n")
                return
            else:
                print("Por favor ingrese un tipo de usuario correcto")


    def buscar_en_usuario(self):
        clear()
        self.abrir_archivo_modo_lectura()
        profesores = self.archivo_profesores.read()
        alumnos = self.archivo_alumnos.read()
        
        for profesor in profesores:
            if self.nombre in profesores and self.apellido in profesor:
                print(nombre, apellido)
                return "Profesor"
            
        for alumno in alumnos:

            if self.nombre in alumnos and self.apellido in alumno:
                return "Alumno"

        print("Usuario no existente")
        return False


def escribir_usuario():
    clear()
    nombre = input("Ingrese su nombre de usuario: ").lower().strip()
    apellido = input("Ingrese su apellido de usuario: ").lower().strip()
    return nombre, apellido

def continuar():
    continuar = input("desea continar: S/N").lower().strip()
    if continuar == "S" or continuar == "s" or continuar == "si" or continuar == "Si":
        return True
    else:
        return False

def buscar_usuario(login):
    while True:
        resultado_busqueda = login.buscar_en_usuario()
        input("enter")
        clear()

        if resultado_busqueda == False:
            login.guardar_usuario()
            input()
            continue
        
        elif resultado_busqueda == "Alumno":
            input("eres alumno")
            if continuar() == False:
                exit()
            else:
                continue
        
        elif resultado_busqueda == "Profesor":
            input("eres profesor")
            if continuar() == False:
                exit()
            else:
                continue
        else:
            continuar


nombre, apellido = escribir_usuario()
login = Login(nombre, apellido)
login.crear_archivos()
buscar_usuario(login)
