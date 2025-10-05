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


def traducir_texto_mymemory(texto, origen="en", destino="es"):
    """
    Traduce un texto usando MyMemory (gratis, con límites).
    """
    url = "https://api.mymemory.translated.net/get"
    params = {"q": texto, "langpair": f"{origen}|{destino}"}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("responseData", {}).get("translatedText", "")
    else:
        return f"Error en la traducción: {response.status_code}"


def traducir_chiste():
    print("¿Desea traducir el chiste? (S/N)")
    respuesta = input("").strip().upper()

    chiste = obtener_chiste()

    if respuesta == "S":
        print("\nRequisando quiste")
        print("\nChiste original en inglés:")
        print(chiste)
        print("\nTraduciendo chiste a español, aguarde un momento...")
        traduccion = traducir_texto_mymemory(chiste, origen="en", destino="es")
        print("\nChiste traducido:")
        print(traduccion)
    else:
        print("\nChiste en inglés:")
        print(chiste)
