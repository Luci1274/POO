import requests
import webbrowser

def dog_api():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        image_url = response.json()["message"]
        print("Precione la URL para visualizar la imagen", image_url)
        return image_url
    else:
        print("Error al obtener la imagen")

def abrir_buscador(image_url):
    print("Habriendo el buscador")
    webbrowser.open(image_url)