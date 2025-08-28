import requests
import webbrowser

def dog_api():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        image_url = response.json()["message"]
        return image_url
    else:
        print("Error al obtener la imagen")

def abrir_buscador(image_url):
    print("Habriendo el buscador")
    webbrowser.open(image_url)

def abrir_imagen():
    image_url = dog_api()
    print("Precione la URL para visualizar la imagen", image_url)
    print("Desea abrir la imagen en el buscador? S/N")
    opcion = input("").strip().upper()
    if opcion == "S":
        abrir_buscador(image_url)
    else:
        print("Ah decidido no hacerlo")
