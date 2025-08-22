import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

import random

class Gerente:
    
    def crear_tarea(self):
        self.tarea = input("Ingrese la tarea: ")
        self.fecha = input("Ingrese la fecha de entrega: ")
        self.hora = input("Ingrese la hora de entrega: ")
        self.descripcion = input("Ingrese la descripcion de la tarea: ")
        self.estado = "Pendiente"
        print(f"Tarea '{self.tarea}' creada con éxito.")
        input("Presione Enter para continuar...")
        return self.tarea
    
    def listado_miembros(self):
        print("Los mienbros del equipo son:")
        miembros = ["Gerardo", "Jorge", "Luis", "Carlos", "Pedro"]
        for miembro in miembros:
            print(f"- {miembro}")
        return miembros
    
    def asignar_tarea(self):
        self.miembros = self.listado_miembros()
        while True:
            miembro_asignado = input("Seleccione el miembro al que desea asignar la tarea:")
            if miembro_asignado in self.miembros:
                clear()
                print(f"Tarea '{self.tarea}' asignada a {miembro_asignado}.")
                input("Presione Enter para continuar...")
                return miembro_asignado
            else:
                clear()
                print("Miembro no encontrado. Por favor, seleccione un miembro de la lista.")
                input("Presione Enter para continuar...")
                self.listado_miembros()
                continue
    
    def revisar_tarea(self):
        clear()
        if self.estado == "Pendiente":
            print(f"Tarea '{self.tarea}' está pendiente.")
            tarea_comleta = False
        elif self.estado == "Completada":
            print(f"Tarea '{self.tarea}' está completada.")
            tarea_completa = True
        elif self.estado == "En Proceso":
            print(f"Tarea '{self.tarea}' está en proceso.")
            tarea_completa = False
        return tarea_completa
        


class Miembro(Gerente):

    def __init__ (self):
        self.tarea = self.crear_tarea()
        clear()
        self.miembro_asignado = self.asignar_tarea()

    def completar_tarea(self):
        clear()
        self.estado = random.choice(["Pendiente", "Completada", "En Proceso"])
        print(f"Tarea '{self.tarea}' marcada como '{self.estado}'.")
        input("Presione Enter para continuar...")
        self.tarea_completa = self.revisar_tarea()
        if self.tarea_completa != True:
            self.completar_tarea()
        else:
            clear()
            print("Tarea completada. Trabajo finalizado.")
    

trabajardor = Miembro()
trabajardor.completar_tarea()