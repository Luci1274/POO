from modulos.menus import Menu_login
from modulos.clases_usuarios import Usuario
from modulos.menu_administrador import menu_administrador
iniciar = Menu_login()

while True:
    nombre, tipo = iniciar.ejecutar()
    if tipo != "administrador":
        usuario = Usuario(nombre)
        usuario.actualizar_informacion()    
    else:
        menu_administrador()
