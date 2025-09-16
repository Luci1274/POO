from modulos.menus import Menu_login
from modulos.clases_usuarios import Usuario
from modulos.menu_administrador import menu_administrador
iniciar = Menu_login()
iniciar.EULA()
while True:
    nombre, tipo = iniciar.ejecutar()
    if tipo != "administrador":
        usuario = Usuario(nombre)
        eliminar = usuario.interactuar_menu()
        if eliminar != True:
            usuario.actualizar_informacion()  
            continue 
        else:
            usuario.eliminar_cuenta()
            continue
    else:
        menu_administrador()
