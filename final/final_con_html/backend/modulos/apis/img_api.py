import requests
import webbrowser

class Apis_imagenes:
    def obtener_imagen(self):
        """
        Método abstracto: debe ser implementado por las clases hijas.

        Debe devolver la URL de la imagen o lanzar RuntimeError en caso de fallo.
        """
        raise NotImplementedError("Este método debe ser implementado en la clase hija.")

    def abrir_buscador(self, image_url):
        """Abre la URL de la imagen en el navegador web predeterminado."""
        webbrowser.open(image_url)

class Dog_api(Apis_imagenes):
    """Obtener imagen de perro de la API Dog."""
    def obtener_imagen(self):
        try:
            url = "https://dog.ceo/api/breeds/image/random"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()["message"]
        except requests.RequestException as exc:
            raise RuntimeError("error al consultar la API de perros") from exc

class Cat_api(Apis_imagenes):
    """Obtener imagen de gato de The Cat API."""
    def obtener_imagen(self):
        try:
            url = "https://api.thecatapi.com/v1/images/search"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data[0]["url"]
        except requests.RequestException as exc:
            raise RuntimeError("error al consultar la API de gatos") from exc


