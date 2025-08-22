import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

class Estudiantes:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__calificaciones = []
        for i in range(2):
            calificaciones = int(input(f"Ingrese la calificación {i + 1} del estudiante: "))
            self.__calificaciones.append(calificaciones)
    
    def modificar_nombre(self):
        while True:
            nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
            if self.__nombre != nuevo_nombre:
                self.__nombre = nuevo_nombre
                print(f"Nombre modificado a: {self.__nombre}")
                break
                
            else:
                print("El nombre ingresado es el mismo que el actual. Intente nuevamente.")
                continue

    def modificar_edad(self):
        while True:
            nueva_edad = int(input("Ingrese la nueva edad del estudiante: "))
            if self.__edad != nueva_edad and nueva_edad > 0:
                self.__edad = nueva_edad
                print(f"Edad modificada a: {self.__edad}")
                break
                
            else:
                print("La edad ingresada es la misma que la actual. Intente nuevamente.")
                continue

    def seleccionar_calificacion(self):
        while True:
            try:
                self.calificacion = int(input("Seleccione la calificación a modificar (1 o 2): "))
                if self.calificacion in [1, 2]:
                    self.calificacion_seleccionada = self.calificacion - 1
                    return self.calificacion_seleccionada
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Entrada no válida. Intente nuevamente.")

    def modificar_calificacion(self):
        self.seleccionar_calificacion()
        while True:
            nueva_calificacion = int(input("Ingrese la nueva calificación del estudiante: "))
            if self.calificacion_seleccionada != nueva_calificacion:
                self.__calificaciones[self.calificacion_seleccionada] = nueva_calificacion
                print(f"Calificación modificada a: {self.__calificaciones}")
                break
                
            else:
                print("La calificación ingresada es la misma que la actual. Intente nuevamente.")
                continue
    
    def promedio_calificaciones(self):
        promedio = sum(self.__calificaciones) / len(self.__calificaciones)
        print(f"El promedio de calificaciones es: {promedio}")
        return promedio
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Calificaciones: {self.__calificaciones}")
        self.promedio_calificaciones()

estudiante = Estudiantes("Juan", 20)
estudiante.mostrar_informacion()
input("Presione Enter para continuar...")
print("Modificando información del estudiante...", "/n")

estudiante.modificar_nombre()
estudiante.modificar_edad()
estudiante.modificar_calificacion()
estudiante.mostrar_informacion()
