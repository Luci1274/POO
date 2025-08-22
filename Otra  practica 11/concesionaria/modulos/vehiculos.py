#importar modulo
from modulos.limpiar_pantalla import clear
import json
import os

class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
    
    def mostrar_info(self):
        return
    
    def guardar_informacion(self):  
        return

class Autos(Vehiculo):
    def __init__(self, marca, modelo, año, precio, tipo_motor):
        super().__init__(marca, modelo, año, precio)
        self.tipo_motor = tipo_motor
    
    def mostrar_info(self):
        clear()
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Precio: {self.precio}")
        print(f"Tipo de motor: {self.tipo_motor}")
    
    def guardar_informacion(self):
        ruta_carpeta = 'datos'  # Define el nombre de la carpeta donde se guardará el archivo.
        ruta_archivo = os.path.join(ruta_carpeta, 'autos.json')  # Une la carpeta y el nombre del archivo para obtener la ruta completa.
        # Crear la carpeta si no existe
        if not os.path.exists(ruta_carpeta):  # Verifica si la carpeta 'datos' no existe.
            os.makedirs(ruta_carpeta)         # Si no existe, la crea.
        # Leer datos existentes
        autos = []  # Inicializa una lista vacía para almacenar los autos.
        if os.path.exists(ruta_archivo) and os.path.getsize(ruta_archivo) > 0:  # Verifica si el archivo existe y no está vacío.
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:  # Abre el archivo en modo lectura.
                try:
                    autos = json.load(archivo)  # Intenta cargar la lista de autos existente desde el archivo.
                except json.JSONDecodeError:
                    autos = []  # Si hay un error al leer el JSON (archivo corrupto o vacío), deja la lista vacía.
        # Agregar el nuevo auto
        autos.append(self.__dict__)  # Agrega el auto actual (convertido a diccionario) a la lista de autos.
        # Guardar la lista actualizada
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:  # Abre el archivo en modo escritura (sobrescribe el archivo).
            json.dump(autos, archivo, indent=4, ensure_ascii=False)  # Guarda la lista de autos en formato JSON, con indentación y caracteres especiales.
        
    def ver_autos_guardados():
            clear()
            ruta_archivo = os.path.join('datos', 'autos.json')
            if os.path.exists(ruta_archivo) and os.path.getsize(ruta_archivo) > 0:
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    autos = json.load(archivo)
                    for auto in autos:
                        print(f"Marca: {auto['marca']}, Modelo: {auto['modelo']}, Año: {auto['año']}, Precio: {auto['precio']}, Tipo de motor: {auto['tipo_motor']}")
            else:
                print("No hay autos guardados.")
                input("Presione Enter para continuar...")

        
class Motocicletas(Vehiculo):
        def __init__(self, marca, modelo, año, precio, tipo_motor):
            super().__init__(marca, modelo, año, precio)
            self.tipo_motor = tipo_motor
        
        def mostrar_info(self):
            clear()
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Año: {self.año}")
            print(f"Precio: {self.precio}")
            print(f"Tipo de motor: {self.tipo_motor}")
        
        def guardar_informacion(self):
            ruta_carpeta = 'datos'
            ruta_archivo = os.path.join(ruta_carpeta, 'motocicletas.json')
            if not os.path.exists(ruta_carpeta):
                os.makedirs(ruta_carpeta)
            motocicletas = []
            if os.path.exists(ruta_archivo) and os.path.getsize(ruta_archivo) > 0:
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    try:
                        motocicletas = json.load(archivo)
                    except json.JSONDecodeError:
                        motocicletas = []
            motocicletas.append(self.__dict__)
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(motocicletas, archivo, indent=4, ensure_ascii=False)
        
        def ver_motocicletas_guardadas():
            clear()
            ruta_archivo = os.path.join('datos', 'motocicletas.json')
            if os.path.exists(ruta_archivo) and os.path.getsize(ruta_archivo) > 0:
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                    motocicletas = json.load(archivo)
                    for moto in motocicletas:
                        print(f"Marca: {moto['marca']}, Modelo: {moto['modelo']}, Año: {moto['año']}, Precio: {moto['precio']}, Tipo de motor: {moto['tipo_motor']}")
            else:
                print("No hay motocicletas guardadas.")
                input("Presione Enter para continuar...")