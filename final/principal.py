from modulos.login import menu_login
from modulos.menu import menu
from modulos.manipular_archivos import GestorDatos

gestos_datos = GestorDatos()

while True:
    nombre_usuario, tipo = menu_login()
    if tipo != "administrador":
        nuevo_ingreso, paginas_visitadas, ultima_pagina_visitada = menu()
        if ultima_pagina_visitada == None or ultima_pagina_visitada == True:
            ultima_pagina_visitada = "ninguna"
            gestos_datos.actualizar_usuario(nombre_usuario, nuevo_ingreso, paginas_visitadas, ultima_pagina_visitada)
        else:
            gestos_datos.actualizar_usuario(nombre_usuario, nuevo_ingreso, paginas_visitadas, ultima_pagina_visitada)
    else:
        "menu_admin()"
