import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

class Forma:

    def area_círculo(self):
        radio = float(input("Introduce el radio del círculo: "))
        area = 3.14 * radio ** 2
        print(f"El área del círculo es: {area}")
    
    def perimetro_círculo(self):
        radio = float(input("Introduce el radio del círculo: "))
        perimetro = 2 * 3.14 * radio
        print(f"El perímetro del círculo es: {perimetro}")

    def area_rectangulo(self):
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        area = base * altura
        print(f"El área del rectángulo es: {area}")
    
    def perimetro_rectangulo(self):
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        perimetro = 2 * (base + altura)
        print(f"El perímetro del rectángulo es: {perimetro}")
    
    def area_triangulo(self):
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")

    def perimetro_triangulo(self):
        lado1 = float(input("Introduce el primer lado del triángulo: "))
        lado2 = float(input("Introduce el segundo lado del triángulo: "))
        base = float(input("Introduce el tercer lado del triángulo: "))
        perimetro = lado1 + lado2 + base
        print(f"El perímetro del triángulo es: {perimetro}")

cambia_formas = Forma()
cambia_formas.area_círculo()
cambia_formas.perimetro_círculo()
input("Preciona Enter para continuar con los rectangulos")
clear()
cambia_formas.area_rectangulo()
cambia_formas.perimetro_rectangulo()
input("Preciona Enter para continuar con los triangulos")
clear()
cambia_formas.area_triangulo()
cambia_formas.perimetro_triangulo()

# Ejercicio 2
input("Preciona Enter para continuar con el ejercicio 2")
clear()
class Cuenta_bancaria:

    def depositar(self):
        self.saldo = 0
        self.cantidad = float(input("Introduce la cantidad a depositar: "))
        self.saldo += self.cantidad
        print(f"El saldo actual es: {self.saldo}")
        return self.saldo
    
    def retirar(self):
        self.cantidad = float(input("Introduce la cantidad a retirar: "))
        if self.cantidad > self.saldo:
            print("No hay suficiente saldo.")
        else:
            self.saldo -= self.cantidad
            print(f"El saldo actual es: {self.saldo}")

quincena = Cuenta_bancaria()
quincena.depositar()
quincena.retirar()

# Ejercicio 3
input("Preciona Enter para continuar con el ejercicio 3")
clear()

class Estudiante:

    def __init__ (self,nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def promedio(self):
        calificaciones = []
        for i in range(3):
            calificacion = float(input(f"Introduce la calificación {i+1}: "))
            calificaciones.append(calificacion)
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"El promedio de {self.nombre} es: {promedio}")

estudiante1 = Estudiante("Juan", 20, "Ingeniería")
estudiante1.promedio()

# Ejercicio 4
input("Preciona Enter para continuar con el ejercicio 4")
clear()

class Libro:

    def __init__ (self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
    
    def datos(self):
        print(f"El libro {self.titulo} fue escrito por {self.autor} y tiene {self.numero_paginas} páginas.")
    
libro1 = Libro("El Quijote", "Miguel de Cervantes", 1000)
libro1.datos()

# Ejercicio 5
input("Preciona Enter para continuar con el ejercicio 5")
clear()

class Vehiculo:

    def __init__ (self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def datos(self):
        print(f"El vehículo es un {self.marca} {self.modelo} del año {self.año}.")

vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo1.datos()

# Ejercicio 6
input("Preciona Enter para continuar con el ejercicio 6")
clear()

class Persona:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def datos(self):
        print(f"La persona se llama {self.nombre} y tiene {self.edad} años.")
    
    def verificar_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")

persona1 = Persona("Juan", 20)
persona1.datos()
persona1.verificar_edad()

# Ejercicio 7
input("Preciona Enter para continuar con el ejercicio 7")
clear()

class Tienda:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.lista_productos = []
    
    def agregar_producto(self):
        while True:
            self.lista_productos.append(input("Introduce el nombre del producto: "))
            print(f"El producto {self.lista_productos[-1]} ha sido agregado a la lista.")
            continuar = input("¿Quieres agregar otro producto? (s/n): ")
            if continuar.lower() != 's':
                break
            else:
                continue

    
    def mostrar_informacion(self):
        print(f"La tienda {self.nombre} tiene los siguientes productos:")
        for producto in self.lista_productos:
            print(f"- {producto}")

tienda1 = Tienda("Tienda de ropa")
tienda1.agregar_producto()
tienda1.mostrar_informacion()

# Ejercicio 8
input("Preciona Enter para continuar con el ejercicio 8")
clear()

class Mascota:
    def __init__ (self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    
    def datos(self):
        print(f"La mascota se llama {self.nombre}, tiene {self.edad} años y es de raza {self.raza}.")

mascota1 = Mascota("Firulais", 5, "Labrador")
mascota1.datos()