from modulos.login import menu_login
from modulos.menu_administrador import menu_administrador
from modulos.menu_usuario import menu_usuario
from modulos.manipular_archivos import Gestor_datos

gestos_datos = Gestor_datos()

while True:
    nombre_usuario, tipo = menu_login()
    if tipo != "administrador":
        nuevo_ingreso, paginas_visitadas, ultima_pagina_visitada = menu_usuario()
        if ultima_pagina_visitada == None or ultima_pagina_visitada == True:
            ultima_pagina_visitada = "ninguna"
            gestos_datos.actualizar_usuario(nombre_usuario, nuevo_ingreso, paginas_visitadas, ultima_pagina_visitada)
        else:
            gestos_datos.actualizar_usuario(nombre_usuario, nuevo_ingreso, paginas_visitadas, ultima_pagina_visitada)
    else:
        menu_administrador()
