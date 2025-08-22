import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

class Empleado:

    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
    
    def mostrar_info(self):
        print(f"El empleado se llama {self.nombre}, se apellida {self.apellido} y su salario es de {self.salario}")

class Gerente(Empleado):

    def __init__(self, nombre, apellido, salario, departamento):
        super().__init__(nombre, apellido, salario)
        self.departamento = departamento
    

    def mostrar_info(self):
        print("\n")
        super().mostrar_info()
        print(f"Además como cuenta con un cargo gerencial, el trabaja en este departamento {self.departamento}")

def agregar_datos():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    salario = int(input("Ingrese el salario: "))        
    return nombre, apellido, salario
nombre, apellido, salario = agregar_datos()

empleado = Empleado(nombre, apellido, salario)
empleado.mostrar_info()

gerente = Gerente(nombre, apellido, salario, 104)
gerente.mostrar_info()