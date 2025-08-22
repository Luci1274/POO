def joke_api():
    import requests

    # Paso 1: Obtener un chiste en inglés desde JokeAPI
    joke_url = "https://v2.jokeapi.dev/joke/Programming?safe-mode"
    response = requests.get(joke_url)

    if response.status_code == 200:
        data = response.json()

        # Extraemos el texto del chiste
        if data["type"] == "single":
            original_text = data["joke"]
        else:
            original_text = f"{data['setup']}\n{data['delivery']}"

        print("Chiste original (inglés):")
        print(original_text)

        # Paso 2: Traducir al español con LibreTranslate
        translate_url = "https://libretranslate.com/translate"

        translate_data = {
            "q": original_text,
            "source": "en",
            "target": "es",
            "format": "text"
        }

        headers = {"Content-Type": "application/json"}

        translation_response = requests.post(translate_url, json=translate_data, headers=headers)

        if translation_response.status_code == 200:
            translated_text = translation_response.json()["translatedText"]
            print("\nChiste traducido (español):")
            print(translated_text)
        else:
            print("Error al traducir:", translation_response.status_code)

    else:
        print("Error al obtener el chiste:", response.status_code)