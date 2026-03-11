from flask import Flask, render_template, jsonify

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

"""la ruta / pertenece al login y el registro de usuarios"""


"""Ruta para renderizar la página de dólar"""
@app.route("/dolar/")
def dolar_page():
    return render_template("dolar.html")

"""API endpoint para obtener datos del dólar en JSON"""
@app.route("/api/dolar/<tipo_dolar>")
def api_dolar(tipo_dolar):
    from modulos.apis.dolar_api import Dolar_oficial, Dolar_tarjeta, Dolar_blue, Dolar_cripto

    if tipo_dolar == "oficial":
        dolar = Dolar_oficial()
        datos = dolar.obtener_datos()
        return jsonify(datos) if isinstance(datos, dict) else jsonify({"datos": datos})

    elif tipo_dolar == "tarjeta":
        dolar = Dolar_tarjeta()
        datos = dolar.obtener_datos()
        return jsonify(datos) if isinstance(datos, dict) else jsonify({"datos": datos})

    elif tipo_dolar == "blue":
        dolar = Dolar_blue()
        datos = dolar.obtener_datos()
        return jsonify(datos) if isinstance(datos, dict) else jsonify({"datos": datos})

    elif tipo_dolar == "cripto":
        dolar = Dolar_cripto()
        datos = dolar.obtener_datos()
        return jsonify(datos) if isinstance(datos, dict) else jsonify({"datos": datos})

    else:
        return jsonify({"error": "Tipo de dólar no válido"}), 400

"""Ruta para renderizar la página de imágenes de perros y gatos"""
@app.route("/imagenes/")
def imagenes():
    return render_template("animales.html")

"""API endpoint para obtener imágenes de perros y gatos en JSON"""
@app.route("/api/imagenes/")
def api_imagenes():
    from modulos.apis.img_api import Dog_api, Cat_api

    try:
        dog_api = Dog_api()
        cat_api = Cat_api()

        dog_image_url = dog_api.obtener_imagen()
        cat_image_url = cat_api.obtener_imagen()

        return jsonify({
            "dog_image": dog_image_url,
            "cat_image": cat_image_url
        })
        
    except RuntimeError as exc:
        return jsonify({"error": str(exc)}), 500

"""Ruta para renderizar la página de juegos free-to-play"""
@app.route("/juegos/")
def juegos():
    return render_template("juegos.html")

"""API endpoint para obtener juegos free-to-play aleatorios en JSON"""
@app.route("/api/juegos/")
def api_juegos():
    from modulos.apis.freetogame_api import Free_to_game_api

    try:
        api = Free_to_game_api()
        juegos_aleatorios = api.obtener_todos(cantidad=5)
        return jsonify(juegos_aleatorios)
    except RuntimeError as exc:
        return jsonify({"error": str(exc)}), 500

"""API endpoint para obtener un juego específico por ID"""
@app.route("/api/juegos/<int:game_id>")
def api_juego_id(game_id):
    from modulos.apis.freetogame_api import Free_to_game_api

    try:
        api = Free_to_game_api()
        juego = api.obtener_por_id(game_id)
        if juego:
            return jsonify(juego)
        else:
            return jsonify({"error": "Juego no encontrado"}), 404
    except RuntimeError as exc:
        return jsonify({"error": str(exc)}), 500

"""API endpoint para obtener el ID máximo disponible"""
@app.route("/api/juegos/max-id/")
def api_juegos_max():
    from modulos.apis.freetogame_api import Free_to_game_api

    try:
        api = Free_to_game_api()
        total = api.contar_juegos()
        return jsonify({"max_id": total})
    except RuntimeError as exc:
        return jsonify({"error": str(exc)}), 500
        

    
"""Correr la aplicación Flask"""
if __name__ == "__main__":
    app.run(debug=True)