import random

class Publicacion:
    def __init__ (self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_informacion(self):
        print(f"Estos son los datos basicos de una publicacion, titulo: {self.titulo}, autor: {self.autor}, año de publicacion: {self.año_publicacion}")

class Libro(Publicacion):
    def __init__(self, titulo, autor, año_publicacion, genero, edad_recomendada):
        super().__init__(titulo, autor, año_publicacion)
        self.genero = genero
        self.edad_recomendada = edad_recomendada
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Ademas un libro contiene los datos: el genero {self.genero}, y la edad recomendada de visualizacion: {self.edad_recomendada}")

    def disponibilidad(self):
        disponibilidad = random.choice([True,False])

        if disponibilidad == True:
            print("El libro está disponible")
        else:
            print("El libro solicitado no está disponible, consulte más tarde")

class Revista(Publicacion):
    def __init__(self, titulo, autor, año_publicacion, tipo, cantidad_paginas):
        super().__init__(titulo, autor, año_publicacion)
        self.__tipo = tipo
        self.__cantidad_paginas = cantidad_paginas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f" Además la revista cuenta con: el tipo de revsita {self.__tipo}, y su cantidad de paginas: {self.__cantidad_paginas} ")
    
    def modificar_cantidad_paginas(self, nueva_cantidad_paginas):
        self.__cantidad_paginas = nueva_cantidad_paginas

class Periodico(Publicacion):
    def __init__(self, titulo, autor, año_publicacion, temas):
        super().__init__(titulo, autor, año_publicacion)
        self.temas = temas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Además el periodico cuenta con la información de los temas a tratar: {self.temas}")

def mostrar_informacion(a):
    a.mostrar_informacion()

def disponibilidad(a):
    a.disponibilidad()

def moficar_cantidad_paginas(a):
    while True:
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad de paginas de la revista:"))  
        except:
            continue
        a.modificar_cantidad_paginas(nueva_cantidad)
        return nueva_cantidad

clear = print("\n" * 50)
while True:
    seleccionar = input("Escriba el elemento que desee: libro, revista, periodico: ").strip().lower()
    if seleccionar == "libro":
        libro = Libro("La historia de la piedra", "Juan", "1894", "historia", 15)
        mostrar_informacion(libro)
        disponibilidad(libro)
        break
    elif seleccionar == "revista": 
        revista = Revista("El mundo de hoy", "Carlos", "2023", "Ocio", 150)
        mostrar_informacion(revista)
        nueva_cantidad = moficar_cantidad_paginas(revista)
        input("Precione enter para continuar con la informacion actualizada")
        mostrar_informacion(revista)
        break
    elif seleccionar == "periodico":
        periodico = Periodico("El mundo", "Marta", "2015", "Cotidianidad") 
        mostrar_informacion(periodico)
        break
    else:
        print("El elemento ingresado no existe o está mal escrito, por favor vuelva a intentarlo")