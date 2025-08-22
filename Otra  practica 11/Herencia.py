def clear():
    import os
    clear = os.system("clear")

class Pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return "{} es un pokemon de tipo {}".format(self.nombre, self.tipo)

class Pikachu(Pokemon):
    def ataque(self, tipoataque):
        return "{} tipo de ataque: {}".format(self.nombre, tipoataque)

class Charmander(Pokemon):
    def ataque(self, tipoataque):
        return "{} tipo de ataque: {}".format(self.nombre, tipoataque)

nuevo_pokemon = Pikachu("body", "electrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("impact trueno"))

class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
    
    def ingresardato(self):
        self.datos = [int(input("ingresar_dato" + str(i+1) + "= ")) for i in range(self.n)]

class Op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
    def suma(self):
        a,b, = self.datos
        s = a + b
        print("el resultado es: ", s)
    
    def resta(self):
        a,b, = self.datos
        s = a - b
        print("el resultado es: ", s)
    
    def multiplicacion(self):
        a,b, = self.datos
        s = a * b
        print("el resultado es: ", s)
    
    def division(self):
        a,b, = self.datos
        s = a / b
        print("el resultado es: ", s)

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)
    
    def cuadrado(self):
        import math
        a, = self.datos
        print("El resultado es:", math.sqrt(a))

clear()

ejemplo = Op_basicas()
print(ejemplo.ingresardato())
print(ejemplo.suma())

ejemplo = Raiz()
ejemplo.ingresardato()
ejemplo.cuadrado()

objeto = Op_basicas()

print(isinstance(objeto, Op_basicas))
print(isinstance(objeto, Raiz))

print(issubclass(Calculadora, Op_basicas))
print(issubclass(Op_basicas, Calculadora))
#print(issubclass(potencia, Calculadora))
print(issubclass(Raiz, Calculadora))

clear()

class Telefono():
    def __init__(selft):
        pass
    
    def llamar(self):
        print("llamando....")
    
    def ocuapado(self):
        print("ocuapdo.....")

class Camara:
    def __init__(self):
        pass

    def fotografia(self):
        print("Tomando fotos......")
    
class Reproduccion:
    def __init__(self):
        pass

    def reproducciones(self):
        print("reproduciendo musica.....")

    def reproducirvideo(self):
        print("reproduciendo video.....")
    
class Smartphone(Telefono, Camara, Reproduccion):
    def __del__(self):
        print("telefono apagado")

movil = Smartphone()
movil.fotografia()
movil.llamar()

clear()

class Auto:
    pass
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return "{} Es un elemento cuatrimotor modelo {}".format(self.marca, self.modelo)

class Taxi(Auto):
    def patente(self, patente):
        return "El taxi modelo {} utiliza la patente: {}".format(self.modelo, patente)

class Patrullero(Auto):
    def patente(self, patente):
        return "El patrullero es un {} y utiliza la patente: {}".format(self.modelo, patente)

nuevo_auto = Taxi("nissan", "2004")
print(nuevo_auto.descripcion())
print(nuevo_auto.patente("123-ABC"))