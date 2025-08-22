import random

class Biblioteca:
    def __init__(self):
        self.catalogo = ["El quijote", "El gato con botas", "Pinoccho"]
        self.usuarios = ["Franco", "Elena", "Mikaela", "juan", "Fer"]

    def agregar_libro(self, libro):
        if not libro in self.catalogo:
            self.catalogo.append(libro)
            print(f"El libro {libro} a sido agregado al catalogo con exito")
        else:
            print(f"El libro ingresado ya existe en el catalogo")
    
    def prestar_libro(self, libro, nombre):
        if not libro in self.catalogo or not nombre in self.usuarios:
            self.agregar_libro(libro)
            self.usuarios.append(nombre)
            print(f"El libro {libro} fue prestado a {nombre}, debe devolverlo en 5 días")
        else:
            print(f"El libro {libro} fue prestado a {nombre}, debe devolverlo en 5 días")

    def devolver_libro(self, libro, nombre):
        if not libro in self.catalogo:
            self.agregar_libro(libro)
            print(f"El libro {libro} a sido devuelto por el usuario {nombre}")
        else:
            print(f"El libro {libro} a sido devuelto por el usuario {nombre}")
    
    def consultar_catalogo(self):
        print(f" Mostrando catalogo disponible")
        for libro in self.catalogo:
            print(f" {libro}")

class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

    def mostrar_titulo(self):
        print(f"Mostrando titulo del libro seleccionado {self.__titulo}")
        titulo = self.__titulo
        return titulo
    
    def mostrar_autor(self):
        print(f"Mostrando autor del libro seleccionado {self.__autor}")
    
    def mostrar_disponiblidad(self):
        if self.__disponible == True:
            print(f"El libro está disponible")
        else:
            print("El libro no está disponible")
    
    def prestar(self, libro, nombre):
        print(f"El usuario {nombre} a tiene el libro {libro}")
        self.__disponible = False
    
    def devolver(self, libro, nombre):
        print(f"El usuario {nombre} a devuelto el libro {libro}")
        self.__disponible = True

class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.lista_libros_prestados = []

    def mostrar_nombre(self):
        print(f"El nombre del usuario es: {self.__nombre}")
        nombre = self.__nombre
        return nombre
    
    def prestar_libro(self, libro):
        nombre = self.mostrar_nombre()
        self.lista_libros_prestados.append(libro)

    def devolver_libro(self, libro):
        try:
            self.lista_libros_prestados.pop(libro)
        except:
            print(f"El libro {libro} no está en posesión del usuario")

class Empleado(Biblioteca):
    def agregar_libro(self, libro):
        nombre_empleado = random.choice(["jose", "Fernando", "Francisco"])
        print(f"{nombre_empleado}, va a agregar un libro")
        super().agregar_libro(libro)
        self.consultar_catalogo()

def continuar():
    continuar = input("desea continuar? s/n").strip().lower()
    if continuar != "s":
            print("Muchas gracias")
            return False
    else:
        return True

def devolver(a,b,c):
    nombre = usuario.mostrar_nombre()
    titulo = libro.mostrar_titulo()
    usuario.devolver_libro(titulo)
    libro.devolver(titulo, nombre)
    biblioteca.devolver_libro(titulo, nombre)
    print ( "-" * 50)

def prestar(a,b,c):
    nombre = usuario.mostrar_nombre()
    titulo = libro.mostrar_titulo()
    usuario.prestar_libro(titulo)
    libro.prestar(titulo, nombre)
    libro.mostrar_disponiblidad()
    biblioteca.prestar_libro(titulo, nombre)

clear = print("\n" * 50, "-" * 50)
while True:
    seleccionar = input("Seleccione la accion a realizar, visualizar catalogo, agregar libro, devolver libro, prestar libro: ").strip().lower()
    if seleccionar == "visualizar catalogo":
        print("\n" * 50, "-" * 50)
        biblioteca = Biblioteca()
        biblioteca.consultar_catalogo()
        print ( "-" * 50)
        if continuar() != True:
            break
    elif seleccionar == "agregar libro":
        clear
        empleado = Empleado()
        libro = Libro("Noche", "Fer")
        titulo = libro.mostrar_titulo()
        empleado.agregar_libro(titulo)
        print ( "-" * 50)
        if continuar() != True:
            break
    elif seleccionar == "devolver libro":
        clear
        usuario = Usuario("juan")
        libro = Libro("Vida", "Carla")
        biblioteca = Biblioteca()
        devolver(usuario, libro, biblioteca)
        if continuar() != True:
            break     
    elif seleccionar == "prestar libro":
        biblioteca = Biblioteca()
        usuario = Usuario("juan")
        libro = Libro("Vida", "Carla")
        devolver(usuario,libro,biblioteca)
        print ( "-" * 50)
        if continuar() != True:
            break     
    else:
        print("Error el texto ingresado no tiene coinciadencia")
        if continuar() != True:
            break