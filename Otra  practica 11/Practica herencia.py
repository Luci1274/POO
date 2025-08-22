def clear():
    import os
    clear = os.system("clear")

class Animal:

    pass
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("waauuuu")
    def descripcion(self):
        return "Me llamo {} y tengo {} años".format(self.nombre , self.edad)
    def cumplir_años(self):
        self.edad = (self.edad + 1)
        print(f"Ayer cumplio años y su nueva edad es: {self.edad}")

    def hablar(self):
        print("wauuu wau waauu (hola señores y señoras)")

clear()

perro = Animal("juan", 5)
print(perro.nombre, perro.edad)
perro.hacer_sonido()
print(perro.descripcion())
perro.cumplir_años()
perro.hablar()

class Perro(Animal):
    pass
    def hablar(self):
        print("wauu (adios)")

perro = Perro("adrian", 3)
perro.hablar()

class Vehiculo:
    pass
    def __init__(self, marca):
        self.marca = marca

class Coche(Vehiculo):
    pass
    def __init__(self, marca, modelo):
        Vehiculo.__init__(self, marca)
        self.modelo = modelo

compacto = Coche("compacto", 4500)
print(compacto.marca, compacto.modelo)

class Persona:
    pass
    def saludar(self):
        print("las personas podemos saludar con la mano")

class Estudiante(Persona):
    pass
    def quejarse(self):
        print("los estudiantes podemos quejarnos de la tarea")

juan = Estudiante()
juan.saludar()
juan.quejarse()

class Figura:
    pass

    def area(self):
        b, = [int(input("ingresar base: "))]
        h, = [int(input("ingresar altura: "))]
        a = b * h
        return "el resultado es: ", a

rectangulo = Figura()
print(rectangulo.area())

class Cuadrado(Figura):
    pass
    def area(self):
        l, = [int(input("ingresar lado: "))]
        a = l * l
        return "el resultado es: ", a

figura_cuadrado = Cuadrado()
print(figura_cuadrado.area())

class Empleado:
    pass
    def trabajar(self):
        print("Trabajo trabajo (dialogo de warcraft 3)")

lopez = Empleado()
lopez.trabajar()

class Gerente(Empleado):
    pass
    def trabajar(self): 
        super().trabajar()
        print("JA JA creen que trabajo")

garcia = Gerente()
garcia.trabajar()

class Producto:
    pass
    def __init__(self,nombre):
        self.nombre = nombre


class Electronico(Producto):
    pass
    def __init__(self, nombre, precio):
        super().__init__(nombre)
        self.precio = precio

telefono_electronico = Electronico("telefono", 1000)
print(telefono_electronico.nombre, telefono_electronico.precio)

class Instrumento:
    pass
    def tocar(self):
        print("Para tocarlo debes de comprarlo")

class Guitarra(Instrumento):
    pass
    def afinar(seld):
        print("El proceso de afinado es algo muy metodico y a gusto del musico")

guitarra = Guitarra()
guitarra.tocar()
guitarra.afinar()

class Libro:
    pass
    def __init__(self, titulo):
        self.titulo = titulo

class Ebook(Libro):
    pass
    def __init__(self, titulo, formato):
        super().__init__(titulo)
        self.formato = formato

l = Ebook("el arte de la guerra", "pdf")
print(l.titulo, l.formato)

class Vehiculo:
    pass
    def moverse(self):
        print("El vehiculo se mueve a 50 km")

class Bicicleta(Vehiculo):
    pass
    def moverse(self):
        super().moverse()
        print("la bicicleta se mueve a 20 km")

becicleta = Bicicleta()
becicleta.moverse()

class Persona:
    def presentarse(self):
        print("Hola, soy .......")

class Profesor(Persona):
    def enseñar(self):
        super().presentarse()
        print("  y soy profesor de matemáticas")

carlos = Profesor()
carlos.enseñar()