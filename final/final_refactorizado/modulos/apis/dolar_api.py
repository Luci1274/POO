from requests.api import request
import requests
from tabulate import tabulate

class Dolar_api:
    def __init__(self, url):
        self.compra = None
        self.venta = None
        self.nombre = None
        self.moneda = None
        self.url = url

    def obtener_datos(self):
        try:
            respuesta = requests.get(self.url)
            respuesta.raise_for_status() # Lanza excepción si hay error HTTP
            datos = respuesta.json()

            self.compra = datos.get("compra")
            self.venta = datos.get("venta")
            self.nombre = datos.get("nombre")
            self.moneda = datos.get("moneda")
        except requests.RequestException as e:
            print(f"Error al consultar la API: {e}")
    
    def mostrar_info(self):
        self.obtener_datos()
        mostrar = [["Dolar:", self.nombre], ["Moneda:", self.moneda], ["Compra:", self.compra], ["Venta:", self.venta]]
        print(tabulate(mostrar,tablefmt="fancy_grid"))

class Dolar_oficial(Dolar_api):
    def __init__(self, url="https://dolarapi.com/v1/dolares/oficial"):
        super().__init__(url)

    
    def obtener_datos(self):
        super().obtener_datos()

    def mostrar_info(self):
        super().mostrar_info()

class Dolar_tarjeta(Dolar_api):
    def __init__(self, url="https://dolarapi.com/v1/dolares/tarjeta"):
        super().__init__(url)
    
    def obtener_datos(self):
        super().obtener_datos()
        
        
    def mostrar_info(self):
        super().mostrar_info()
        

class Dolar_blue(Dolar_api):
    def __init__(self, url="https://dolarapi.com/v1/dolares/blue"):
        super().__init__(url)

    def obtener_datos(self):
        super().obtener_datos()
        
        
    def mostrar_info(self):
        super().mostrar_info()

class Dolar_cripto(Dolar_api):
    def __init__(self, url="https://dolarapi.com/v1/dolares/cripto"):
        super().__init__(url)
    
    def obtener_datos(self):
        super().obtener_datos()
    
    def mostrar_info(self):
        super().mostrar_info()