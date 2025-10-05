import requests
import webbrowser

class Apis_imagenes:
    def obtener_imagen(self):
        """
        Método abstracto: debe ser implementado por las clases hijas
        """
        raise NotImplementedError("Este método debe ser implementado en la clase hija.")

    def abrir_buscador(self, image_url):
        print("Abriendo el buscador...")
        webbrowser.open(image_url)

    def abrir_imagen(self):
        image_url = self.obtener_imagen()
        if image_url:
            print("Presione la URL para visualizar la imagen:", image_url)
            opcion = input("¿Desea abrir la imagen en el buscador? (S/N): ").strip().upper()
            if opcion == "S":
                self.abrir_buscador(image_url)
            else:
                print("Ha decidido no hacerlo.")
        else:
            print("No se pudo obtener la imagen.")


class Dog_api(Apis_imagenes):
    def obtener_imagen(self):
        url = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["message"]
        else:
            print("Error al obtener la imagen de perro.")
            return None


class Cat_api(Apis_imagenes):
    def obtener_imagen(self):
        url = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data[0]["url"]
        else:
            print("Error al obtener la imagen de gato.")
            return None



