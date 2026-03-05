import requests
import random

class Free_to_game_api:
    BASE_URL = "https://www.freetogame.com/api"

    def obtener_todos(self, cantidad=5):
        """
        Obtiene una lista de juegos free-to-play (aleatorios, limitados a 'cantidad').

        Devuelve una lista de diccionarios de juego o lanza una excepción en caso de fallo.
        """
        try:
            url = f"{self.BASE_URL}/games"
            response = requests.get(url)
            response.raise_for_status()
            juegos = response.json()
            if len(juegos) >= cantidad:
                return random.sample(juegos, cantidad)  # aleatorios sin repetidos
            return juegos  # si hay menos juegos de los pedidos
        except requests.RequestException as exc:
            raise RuntimeError("no se pudo consultar la API de FreeToGame") from exc

    def obtener_por_id(self, game_id):
        """
        Obtiene un juego específico por ID.

        Devuelve el diccionario del juego o None si no existe. Lanza excepción en caso de
        error de red o HTTP.
        """
        try:
            url = f"{self.BASE_URL}/game?id={game_id}"
            response = requests.get(url)
            response.raise_for_status()
            juego = response.json()
            return juego or None
        except requests.RequestException as exc:
            raise RuntimeError(f"error al consultar la API para el juego {game_id}") from exc
    
    def contar_juegos(self):
        """
        Devuelve la cantidad total de juegos disponibles en FreeToGame.

        Lanza excepción en caso de error de red o HTTP.
        """
        try:
            url = f"{self.BASE_URL}/games"
            response = requests.get(url)
            response.raise_for_status()
            juegos = response.json()
            return len(juegos)
        except requests.RequestException as exc:
            raise RuntimeError("no se pudo obtener el total de juegos") from exc