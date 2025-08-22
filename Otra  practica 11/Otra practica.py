class Auto():
    marca = ""
    modelo = 2004
    placa = ""

taxi = Auto()
print(taxi.modelo)

class Jugadores_A:
    j1 = "messi"
    j2 = "c.ronaldo"
class Jugadores_B:
    j3 = "marcelo"
    j1 = "falcao"

print(Jugadores_B.j1)

class Auto_taxi:
    marca = "nissan"
    modelo = 2004
    Placa = "123-ABC"
class Auto_patrullero:
    marca = "toyota"
    modelo = 2017
    Placa = "789-XYZ"
print("Es un taxi modelo:", Auto_taxi.modelo, "y su marca es:", Auto_taxi.marca)
print("Es un patrullero modelo", Auto_patrullero.modelo,"y su mplaca es:" , Auto_patrullero.Placa)

class Nombre:
    pass

victor = Nombre()
maria = Nombre()

victor.edad = 30
victor.sexo = "masculino"
victor.pais = "Bolivia"
maria.edad = 25
maria.sexo = "femenino"
maria.pais = "Colombia"

print("la edad de victor es:", victor.edad, "y la edad de maria es:" , maria.edad)

class Auto_nuevo:
    pass

taxi = Auto_nuevo()
patrullero = Auto_nuevo()

taxi.marca = "nissan"
taxi.modelo = 2004
taxi.Placa = "123-ABC"
patrullero.marca = "toyota"
patrullero.modelo = 2017
patrullero.Placa = "789-XYZ"

print("tenemos un taxi con las caracteristicas","\n" , taxi.modelo,"\n" , taxi.marca ,"\n", taxi.Placa,"\n" , "Y un patrullero con las caracteristicas","\n" , patrullero.modelo,"\n" , patrullero. marca,"\n" , patrullero.Placa)

class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3

s = Matematica()
s.suma()
print(s.n1 + s.n2)

class Auto_3():
    def caracteristicas(self):
        self.marca = "nissan"
        self.modelo = 2004
        self.placa = "123-ABC"

taxi = Auto_3()
taxi.caracteristicas()
print("La marca del taxi es: ", taxi.marca, "el modelo del taxi es: ",  taxi.modelo, "la placa del taxi es", taxi.placa)

class Ropa:
    def __init__ (self):
        self.marca = "willow"
        self.talla = "M"
        self.color = "rojo"

camisa = Ropa()
print(camisa.marca)
print(camisa.color)
print(camisa.talla)

class Auto_4():
    def __init__ (self):
        self.marca = "nissan"
        self.modelo = 2004
        self.Placa = "123-ABC"

taxi = Auto_4()
print(taxi.marca, taxi.modelo, taxi.Placa)

class Calculadora:
    def __init__ (self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

operacion = Calculadora(12, 13)
print(operacion.suma)

class Persona:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

persona = Persona("Juan", 30)
persona.saludar()

class Auto_5:
    def __init__ (self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
    def introduccion_taxi(self):
        print(f"Este es mí taxi y es marca {self.marca}, su modelo es {self.modelo} y su placa es {self.placa} si lo ven llamar al ...... ")
    def introduccion_patrullero(self):
        print(f"Hola somos la policia nosotros utilizamos autos marca {self.marca}, el modelo de esta patrulla es {self.modelo} y su placa es {self.placa}")

taxi = Auto_5("nissan", 2004, "123-ABC")
taxi.introduccion_taxi()
patrullero = Auto_5("toyota", 2017, "789-XYZ")
patrullero.introduccion_patrullero()

class Persona_2:
    edad = 27
    nombre = "Victor"
    pais = "Brazil"

doctor = Persona_2()
print("la edad es: ", doctor.edad)
print("la edad es: ", getattr(doctor, "edad"))
print("el doctor tiene una edad:", hasattr(doctor, "edad"))
print("el doctor tiene una edad:", hasattr(doctor, "apellido"))
print("antes era:", doctor.nombre)
setattr( doctor, "nombre", "Hector")
print("ahora se llama", doctor.nombre)
delattr(Persona_2, "pais")

class Persona_2:
    def __init__ (self, nombre, año):
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        return "{} tiene {}".format(self.nombre, self.año)
    def comentario(self, frase):
        return "{} dice: {}".format(self.nombre, frase)

doctor = Persona_2("Gerardo", 20)
print(doctor.nombre)
print(doctor.descripcion())
print(doctor.comentario("esta es la frase que yo dije"))

class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()
print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)
