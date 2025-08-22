#Sistema de gestion de biblioteca

import os

def clear():
    clear = os.system("cls")
    return

clear()

class Material:
    def __init__ (self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def mostrar_info(self):
        return

class Libro(Material):
    def __init__ (self, titulo, autor, año, ISBN):
        super().__init__(titulo, autor, año)
        self.ISBN = ISBN

    def mostrar_info(self):
        print(f"Mostrando informacion del libro\n"
        f"Titulo: {self.titulo}\n"
        f"Autor: {self.autor}\n"
        f"Año: {self.año}\n"
        f"ISBN: {self.ISBN}")

class Revista(Material):
    def __init__ (self, titulo, autor, año, numero_de_edicion):
        super().__init__(titulo, autor, año)
        self.numero_de_edicion = numero_de_edicion

    def mostrar_info(self):
        print(f"Mostrando informacion de la revista\n"
        f"Titulo: {self.titulo}\n"
        f"Autor: {self.autor}\n"
        f"Año: {self.año}\n"
        f"Numero de edicion: {self.numero_de_edicion}")

class Usuario:
    def __init__ (self, nombre, ID):
        self.__nombre = nombre
        self.__ID = ID
        self.libros_en_posesion = []
    
    def prestar(self, libro):
        self.libros_en_posesion.append(libro)
    
    def devolver(self, libro):
        self.libros_en_posesion.remove(libro)

class Biblioteca:
    def __init__ (self):
        self.materiales = {}
        self.usuarios = {}
    
    def agregar_material(self):
        tipo = input("Ingrese el tipo de material (libro/revuista): ").lower().strip()
        titulo = input("Ingrese el titulo: ").strip()
        autor = input("Ingrese el autor: ").strip()
        año = input("Ingrese el año: ").strip()
        if tipo == "libro":
            ISBN = input("Ingrese el ISBN: ").strip()
            material = Libro(titulo, autor, año, ISBN)
            self.materiales[titulo] = autor, año, ISBN
            print(f"Material {titulo} agregado exitosamente.")
        elif tipo == "revista":
            numero_de_edicion = input("Ingrese el numero de edicion: ").strip()
            material = Revista(titulo, autor, año, numero_de_edicion)
            self.materiales[titulo] = autor, año, numero_de_edicion
            print(f"Material {titulo} agregado exitosamente.")
        else:
            print("Tipo de material no reconocido.")
            return
    
    def registrar_usuarios(self):
        nombre = input("Ingrese el nombre del usuario: ").strip()
        ID = input("Ingrese el ID del usuario: ").strip()
        usuario = Usuario(nombre, ID)
        self.usuarios[ID] = usuario
        print(f"Usuario {nombre} registrado con ID {ID}.")
        return usuario
    
    def prestar_material(self):
        ID = input("Ingrese el ID del usuario: ").strip()
        if ID not in self.usuarios:
            print("Usuario no encontrado.")
            return
        titulo = input("Ingrese el titulo del material a prestar: ").strip()
        if titulo not in self.materiales:
            print("Material no encontrado.")
            return
        usuario = self.usuarios[ID]
        material = self.materiales[titulo]
        usuario.prestar(material)
        print(f"Material {titulo} prestado a {self.usuarios[usuario]}.")
        return usuario
    
    def devolver_material(self):
        ID = input("Ingrese el ID del usuario: ").strip()
        if ID not in self.usuarios:
            print("Usuario no encontrado.")
            return
        titulo = input("Ingrese el titulo del material a devolver: ").strip()
        usuario = self.usuarios[ID]
        if titulo not in usuario.libros_en_posesion:
            print("El usuario no tiene este material en posesion.")
            return
        usuario.devolver(titulo)
        print(f"Material {titulo} devuelto por {self.usuarios[usuario]}.")
        return usuario
    
    def mostrar_materiales(self):
        if not self.materiales:
            print("No hay materiales registrados.")
            return
        else:
            print("Materiales registrados:")
            for titulo, info in self.materiales.items():
                autor, año, extra = info
                print(f"Titulo: {titulo}, Autor: {autor}, Año: {año}, Extra: {extra}")
        return
    
def elegir_opcion():
    print("Sistema de gestion de biblioteca")
    print("1. Agregar material")
    print("2. Registrar usuario")
    print("3. Prestar material")
    print("4. Devolver material")
    print("5. Salir")
    
    opcion = input("Seleccione una opcion: ").strip()
    return opcion
def main():
    biblioteca = Biblioteca()
    while True:
        opcion = elegir_opcion()
        
        if opcion == "1":
            .agregar_matebibliotecarial()
        
        elif opcion == "2":
            usuario = biblioteca.registrar_usuarios()
        
        elif opcion == "3":
            biblioteca.mostrar_materiales()
            biblioteca.prestar_material()
        

        elif opcion == "4":
            biblioteca.devolver_material()
       
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
       
        else:
            print("Opcion no valida, intente de nuevo.")
        clear()

main()
