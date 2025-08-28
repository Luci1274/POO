from modulos.login import menu_login
from modulos.menu import menu
from modulos.manipular_archivos import GestorDatos

gestos_datos = GestorDatos()

while True:
    nombre_usuario = menu_login()
    nuevo_ingreso, paginas_visitadas, ultima_pagina_visitada = menu()
    gestos_datos.actualizar_usuario(nombre_usuario, nuevo_ingreso, paginas_visitadas, ultima_pagina_visitada)
