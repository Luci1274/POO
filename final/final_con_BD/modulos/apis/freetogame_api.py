import requests
from tabulate import tabulate
import random

class Free_to_game_api:
    BASE_URL = "https://www.freetogame.com/api"

    def obtener_todos(self, cantidad=5):
        """
        Obtiene una lista de juegos free-to-play (aleatorios, limitados a 'cantidad')
        """
        url = f"{self.BASE_URL}/games"
        response = requests.get(url)
        if response.status_code == 200:
            juegos = response.json()
            if len(juegos) >= cantidad:
                seleccionados = random.sample(juegos, cantidad)  # aleatorios sin repetidos
            else:
                seleccionados = juegos  # si hay menos juegos de los pedidos
            self.mostrar_tabla(seleccionados)
            return seleccionados
        else:
            print("Error al obtener los juegos.")
            return []

    def obtener_por_id(self, game_id):
        """
        Obtiene un juego específico por ID
        """
        url = f"{self.BASE_URL}/game?id={game_id}"
        response = requests.get(url)
        if response.status_code == 200:
            juego = response.json()
            if not juego:
                print("No hay datos para mostrar.")
                return
            tabla = []
            tabla.append([juego["id"], juego["title"], juego["genre"], juego["platform"]])
            print(tabulate(tabla, headers=["ID", "Título", "Género principal", "Plataforma"], tablefmt="fancy_grid"))
                
        else:
            print("Error al obtener el juego.")
            return None
    
    def contar_juegos(self):
        """
        Devuelve la cantidad total de juegos disponibles en FreeToGame
        """
        url = f"{self.BASE_URL}/games"
        response = requests.get(url)
        if response.status_code == 200:
            juegos = response.json()
            return len(juegos)
        else:
            print("Error al obtener el total de juegos.")
            return 0

    def mostrar_tabla(self, juegos):
        """
        Muestra los juegos en una tabla usando tabulate
        """
        if not juegos:
            print("No hay datos para mostrar.")
            return
        tabla = []
        for juego in juegos:
            tabla.append([juego["id"], juego["title"], juego["genre"], juego["platform"]])
        print(tabulate(tabla, headers=["ID", "Título", "Género principal", "Plataforma"], tablefmt="fancy_grid"))

api = Free_to_game_api()
api.obtener_por_id(5)