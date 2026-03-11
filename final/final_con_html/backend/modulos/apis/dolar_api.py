from requests.api import request
import requests

class Dolar_api:
    def __init__(self, url):
        self.url = url

    def obtener_datos(self):
        """Obtiene los datos de la API de dólar según la URL proporcionada"""
        try:
            respuesta = requests.get(self.url)
            respuesta.raise_for_status() # Lanza excepción si hay error HTTP
            return respuesta.json()
            
        except requests.RequestException as e:
            raise RuntimeError(f"Error al obtener datos de la API") from e

class Dolar_oficial(Dolar_api):
    def __init__(self, url="https://dolarapi.com/v1/dolares/oficial"):
        super().__init__(url)

    
    def obtener_datos(self):
        return super().obtener_datos()


class Dolar_tarjeta(Dolar_api):
    def __init__(self, url="https://dolarapi.com/v1/dolares/tarjeta"):
        super().__init__(url)
    
    def obtener_datos(self):
        return super().obtener_datos()
        

class Dolar_blue(Dolar_api):
    def __init__(self, url="https://dolarapi.com/v1/dolares/blue"):
        super().__init__(url)

    def obtener_datos(self):
        return super().obtener_datos()
        

class Dolar_cripto(Dolar_api):
    def __init__(self, url="https://dolarapi.com/v1/dolares/cripto"):
        super().__init__(url)
    
    def obtener_datos(self):
        return super().obtener_datos()
