import requests

def obtener_chiste():
    """
    Obtiene un chiste en inglés desde JokeAPI.
    """
    url = "https://v2.jokeapi.dev/joke/Programming?safe-mode"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["type"] == "single":
            return data["joke"]
        elif data["type"] == "twopart":
            return f"{data['setup']} ... {data['delivery']}"
    else:
        return "Error al obtener el chiste."


def traducir_texto(texto, origen="en", destino="es"):
    """
    Traduce un texto usando la API de LibreTranslate.
    - origen: idioma original (ej. 'en' para inglés).
    - destino: idioma de traducción (ej. 'es' para español).
    """
    url = "https://libretranslate.com/translate"
    payload = {
        "q": texto,
        "source": origen,
        "target": destino,
        "format": "text"
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["translatedText"]
    else:
        return "Error en la traducción."

def traducir_chiste():
    print("Desea traducir el chiste? S/N")
    respuesta = input("").strip().upper()
    if respuesta != "N" or respuesta == "N":
        chiste = obtener_chiste()
        print(chiste)
    elif respuesta == "S":
        chiste = obtener_chiste()
        traduccion = traducir_texto(chiste, origen="en", destino="es")
        print("\nChiste traducido al español:")
        print(traduccion)