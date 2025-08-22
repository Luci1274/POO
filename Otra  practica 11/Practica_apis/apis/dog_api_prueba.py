def dog_api():
    import requests
    import webbrowser

    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        image_url = response.json()["message"]
        print("Abriendo imagen:", image_url)
        webbrowser.open(image_url)
    else:
        print("Error al obtener la imagen")