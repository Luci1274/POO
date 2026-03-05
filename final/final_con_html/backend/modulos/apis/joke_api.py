import requests

class JokeApi:
    """
    Clase para obtener chistes de programación desde JokeAPI y traducirlos.
    """

    def obtener_chiste(self):
        """
        Obtiene un chiste en inglés desde JokeAPI.

        Returns:
            str: El chiste en formato de texto (single o twopart).

        Raises:
            RuntimeError: Si falla la consulta a la API.
        """
        # Definir la URL de la API de chistes (categoría Programming, modo seguro)
        url = "https://v2.jokeapi.dev/joke/Programming?safe-mode"

        # Hacer la solicitud GET a la API
        response = requests.get(url)

        # Verificar si la respuesta es exitosa (código 200)
        if response.status_code == 200:
            # Convertir la respuesta JSON a un diccionario Python
            data = response.json()

            # Si el chiste es de tipo 'single' (un solo párrafo), devolverlo directamente
            if data["type"] == "single":
                return data["joke"]
            # Si es 'twopart' (setup y delivery), combinarlos en un string
            elif data["type"] == "twopart":
                return f"{data['setup']} ... {data['delivery']}"
        else:
            # Si hay error en la respuesta, lanzar una excepción con detalles
            raise RuntimeError(f"Error al obtener el chiste: {response.status_code}")

    def traducir_texto_mymemory(self, texto, origen="en", destino="es"):
        """
        Traduce un texto usando la API gratuita de MyMemory.

        Args:
            texto (str): El texto a traducir.
            origen (str): Idioma de origen (por defecto 'en' para inglés).
            destino (str): Idioma de destino (por defecto 'es' para español).

        Returns:
            str: El texto traducido.

        Raises:
            RuntimeError: Si falla la traducción.
        """
        # URL de la API de traducción MyMemory
        url = "https://api.mymemory.translated.net/get"

        # Parámetros para la solicitud: texto, par de idiomas
        params = {"q": texto, "langpair": f"{origen}|{destino}"}

        # Hacer la solicitud GET con los parámetros
        response = requests.get(url, params=params)

        # Verificar si la respuesta es exitosa
        if response.status_code == 200:
            # Convertir respuesta JSON
            data = response.json()

            # Extraer el texto traducido del diccionario de respuesta
            translated = data.get("responseData", {}).get("translatedText", "")

            # Si no hay traducción, devolver un mensaje de error
            if not translated:
                raise RuntimeError("No se pudo obtener la traducción")

            return translated
        else:
            # Lanzar excepción si hay error HTTP
            raise RuntimeError(f"Error en la traducción: {response.status_code}")

    def obtener_chiste_y_traduccion(self):
        """
        Obtiene un chiste en inglés y su traducción al español.

        Returns:
            dict: Un diccionario con 'original' (chiste en inglés) y 'traducido' (chiste en español).

        Raises:
            RuntimeError: Si falla la obtención del chiste o la traducción.
        """
        # Primero, obtener el chiste original en inglés
        chiste_original = self.obtener_chiste()

        # Luego, traducir el chiste al español usando MyMemory
        chiste_traducido = self.traducir_texto_mymemory(chiste_original)

        # Devolver un diccionario con ambos textos
        return {
            "original": chiste_original,
            "traducido": chiste_traducido
        }
