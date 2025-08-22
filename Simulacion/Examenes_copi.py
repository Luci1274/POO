import os
import csv

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Clases de Usuario ---
class Usuario:
    def __init__(self, nombre, contraseña):
        self._nombre = nombre
        self._contraseña = contraseña

    @property
    def nombre(self):
        return self._nombre

    def verificar_contraseña(self, contraseña):
        return self._contraseña == contraseña

class Profesor(Usuario):
    def __init__(self, nombre, contraseña):
        super().__init__(nombre, contraseña)

class Estudiante(Usuario):
    def __init__(self, nombre, contraseña):
        super().__init__(nombre, contraseña)

# --- Clases de Pregunta ---
class Pregunta:
    def __init__(self, enunciado, puntos):
        self.enunciado = enunciado
        self.puntos = puntos

    def evaluar(self, respuesta):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def to_csv(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    @staticmethod
    def from_csv(row):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class PreguntaOpcionMultiple(Pregunta):
    def __init__(self, enunciado, opciones, correcta, puntos):
        super().__init__(enunciado, puntos)
        self.opciones = opciones
        self.correcta = correcta

    def evaluar(self, respuesta):
        if respuesta == self.correcta:
            return self.puntos, "Correcto"
        else:
            return 0, f"Incorrecto. Respuesta correcta: {self.correcta}"

    def to_csv(self):
        return ["opcion", self.enunciado, "|".join(self.opciones), self.correcta, str(self.puntos)]

    @staticmethod
    def from_csv(row):
        return PreguntaOpcionMultiple(row[1], row[2].split("|"), row[3], int(row[4]))

class PreguntaVerdaderoFalso(Pregunta):
    def __init__(self, enunciado, correcta, puntos):
        super().__init__(enunciado, puntos)
        self.correcta = correcta

    def evaluar(self, respuesta):
        if respuesta.lower() == self.correcta.lower():
            return self.puntos, "Correcto"
        else:
            return 0, f"Incorrecto. Respuesta correcta: {self.correcta}"

    def to_csv(self):
        return ["vf", self.enunciado, self.correcta, str(self.puntos)]

    @staticmethod
    def from_csv(row):
        return PreguntaVerdaderoFalso(row[1], row[2], int(row[3]))

class PreguntaAbierta(Pregunta):
    def __init__(self, enunciado, puntos):
        super().__init__(enunciado, puntos)

    def evaluar(self, respuesta):
        return None, "Pendiente de corrección manual"

    def to_csv(self):
        return ["abierta", self.enunciado, str(self.puntos)]

    @staticmethod
    def from_csv(row):
        return PreguntaAbierta(row[1], int(row[2]))

# --- Clase Examen ---
class Examen:
    def __init__(self, nombre, creador):
        self.nombre = nombre
        self.creador = creador
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def guardar(self):
        with open(f"{self.nombre}_examen.csv", "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            for p in self.preguntas:
                writer.writerow(p.to_csv())

    def cargar(self):
        self.preguntas = []
        with open(f"{self.nombre}_examen.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                tipo = row[0]
                if tipo == "opcion":
                    self.preguntas.append(PreguntaOpcionMultiple.from_csv(row))
                elif tipo == "vf":
                    self.preguntas.append(PreguntaVerdaderoFalso.from_csv(row))
                elif tipo == "abierta":
                    self.preguntas.append(PreguntaAbierta.from_csv(row))

    def evaluar(self, respuestas):
        puntaje = 0
        feedback = []
        for pregunta, respuesta in zip(self.preguntas, respuestas):
            puntos, fb = pregunta.evaluar(respuesta)
            if puntos is not None:
                puntaje += puntos
            feedback.append(fb)
        return puntaje, feedback

# --- Funciones de autenticación y menú ---
def cargar_usuarios(nombre_archivo):
    usuarios = []
    with open(nombre_archivo, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == "profesor":
                usuarios.append(Profesor(row[0], row[1]))
            else:
                usuarios.append(Estudiante(row[0], row[1]))
    return usuarios

def guardar_usuario(nombre_archivo, usuario, tipo):
    with open(nombre_archivo, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([usuario._nombre, usuario._contraseña, tipo])

def login(usuarios):
    nombre = input("Usuario: ")
    contraseña = input("Contraseña: ")
    for u in usuarios:
        if u.nombre == nombre and u.verificar_contraseña(contraseña):
            return u
    print("Usuario o contraseña incorrectos.")
    return None

def menu_profesor(profesor):
    print(f"\nBienvenido, Profesor {profesor.nombre}")
    nombre_examen = input("Nombre del nuevo examen: ")
    examen = Examen(nombre_examen, profesor.nombre)
    while True:
        print("\n1. Agregar pregunta opción múltiple")
        print("2. Agregar pregunta verdadero/falso")
        print("3. Agregar pregunta abierta")
        print("4. Guardar examen y salir")
        op = input("Opción: ")
        if op == "1":
            enunciado = input("Enunciado: ")
            opciones = [input(f"Opción {i+1}: ") for i in range(4)]
            correcta = input("Respuesta correcta: ")
            puntos = int(input("Puntos: "))
            examen.agregar_pregunta(PreguntaOpcionMultiple(enunciado, opciones, correcta, puntos))
        elif op == "2":
            enunciado = input("Enunciado: ")
            correcta = input("Respuesta (verdadero/falso): ")
            puntos = int(input("Puntos: "))
            examen.agregar_pregunta(PreguntaVerdaderoFalso(enunciado, correcta, puntos))
        elif op == "3":
            enunciado = input("Enunciado: ")
            puntos = int(input("Puntos: "))
            examen.agregar_pregunta(PreguntaAbierta(enunciado, puntos))
        elif op == "4":
            examen.guardar()
            print("Examen guardado.")
            break

def menu_estudiante(estudiante):
    print(f"\nBienvenido, Estudiante {estudiante.nombre}")
    nombre_examen = input("Nombre del examen a realizar: ")
    examen = Examen(nombre_examen, "")
    try:
        examen.cargar()
    except FileNotFoundError:
        print("Examen no encontrado.")
        return
    respuestas = []
    for pregunta in examen.preguntas:
        print(f"\n{pregunta.enunciado}")
        if isinstance(pregunta, PreguntaOpcionMultiple):
            for idx, op in enumerate(pregunta.opciones):
                print(f"{idx+1}. {op}")
            resp = input("Respuesta: ")
            respuesta = pregunta.opciones[int(resp)-1] if resp.isdigit() and 1 <= int(resp) <= len(pregunta.opciones) else ""
        elif isinstance(pregunta, PreguntaVerdaderoFalso):
            respuesta = input("Respuesta (verdadero/falso): ")
        else:
            respuesta = input("Respuesta: ")
        respuestas.append(respuesta)
    puntaje, feedback = examen.evaluar(respuestas)
    print(f"\nPuntaje automático: {puntaje}")
    print("Feedback:")
    for fb in feedback:
        print(fb)
    # Guardar reporte
    with open(f"{estudiante.nombre}_{nombre_examen}_reporte.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Pregunta", "Respuesta", "Feedback"])
        for p, r, fb in zip(examen.preguntas, respuestas, feedback):
            writer.writerow([p.enunciado, r, fb])

# --- Main ---
def main():
    usuarios = []
    archivo_usuarios = "usuarios.csv"
    # Crear archivo de usuarios si no existe
    if not os.path.exists(archivo_usuarios):
        with open(archivo_usuarios, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "contraseña", "tipo"])
    # Cargar usuarios
    usuarios = cargar_usuarios(archivo_usuarios)
    print("1. Registrarse\n2. Iniciar sesión")
    op = input("Opción: ")
    if op == "1":
        nombre = input("Nombre: ")
        contraseña = input("Contraseña: ")
        tipo = input("Tipo (profesor/estudiante): ")
        if tipo == "profesor":
            usuario = Profesor(nombre, contraseña)
        else:
            usuario = Estudiante(nombre, contraseña)
        guardar_usuario(archivo_usuarios, usuario, tipo)
        print("Usuario registrado. Inicia sesión para continuar.")
        return
    elif op == "2":
        usuario = login(usuarios)
        if usuario:
            if isinstance(usuario, Profesor):
                menu_profesor(usuario)
            else:
                menu_estudiante(usuario)

if __name__ == "__main__":
    main()