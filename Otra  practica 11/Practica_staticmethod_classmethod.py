#Ejercicio 1: definir un método estático

class MiClase:
    
    @staticmethod
    def metodo_estatico():
        print("Este es un método estático")

# Llamada al método estático
MiClase.metodo_estatico()

input("Presiona Enter para continuar...")
#Ejercicio 2: definir un método de clase

class MiClase:
    @classmethod
    def metodo_de_clase(cls):
        print("Ese es un método de clase")

# Llamada al método de clase
MiClase().metodo_de_clase()

input("Presiona Enter para continuar...")
#Ejercicio 3: definir un método de instancia

class Calculadora:

    @staticmethod
    def sumar(a, b):
        return a + b
    
# Usar método estático para sumar dos números

resultado = Calculadora.sumar(5, 3)
print(resultado)

input("Presiona Enter para continuar...")
#Ejercicio 4: definir un método de clase que devuelva una instancia de la clase

class Persona:
    def __init__(self,nombre):
        self.nombre = nombre

    @classmethod
    def crear(cls, nombre):
        return cls(nombre)

# Usar el método de clase para crear una isntancia de Persona

persona = Persona.crear("Juan")
print(persona.nombre)

input("Presiona Enter para continuar...")

#Ejercicio 5: comparar métodos estáticos y de clase

class MiClase:
    atributo_clase = "Soy un atribuo de clase"

    @staticmethod
    def metodo_estatico():
        print("Método estático")

    @classmethod
    def metodo_de_clase(cls):
        print("Método de clase: ", cls.atributo_clase)
    
# Llamar a los métodos y comparar resultados
MiClase.metodo_estatico()
MiClase.metodo_de_clase()

input("Presiona Enter para continuar...")
#Ejercicio 6: Usar métodos estáticos como utilidades

class Utilidades:

    @staticmethod
    def convertir_a_mayusculas(texto):
        return texto.upper()

# Usar el metodo estático para convertir un texto a mayúsculas
texto = "hola mundo"
texto_mayusculas = Utilidades.convertir_a_mayusculas(texto)
print(texto_mayusculas)

input("Presiona Enter para continuar...")
#Ejercicio 7: Usar métodos de clase para inicialización alternativa

class Fecha:
    def __init__ (self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    @classmethod
    def desde_cadena(cls, cadena_fecha):
        dia, mes, año = map(int, cadena_fecha.split("-"))
        return cls(dia, mes, año)
    
# Usar el método de clase para crear una instacia de fecha desde una cade
fecha = Fecha.desde_cadena("25-12-2023")
print(fecha.dia, fecha.mes, fecha.año)

input("Presiona Enter para continuar...")
#Ejercicio 8: Definir métodos estáticos y de clase en la misma clase

class MiClase:
    def __init__ (self, valor):
        self.valor = valor

    @staticmethod
    def metodo_estatico():
        print("Método estático llamado")

    @classmethod
    def metodo_de_clase(cls, valor):
        return cls(valor)

# Llamada a método estático y de clase
MiClase.metodo_estatico()
objeto = MiClase.metodo_de_clase(10)
print(objeto.valor)

input("Presiona Enter para continuar...")
#Ejercicio 9: Usar métodos estáticos para validación

class Validador:
    
    @staticmethod
    def es_numero_positivo(numero):
        return numero > 0

# Usar el método estático para validar si un número es positivo
numero = -5
es_positivo = Validador.es_numero_positivo(numero)
print(es_positivo)
