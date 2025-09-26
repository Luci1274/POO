from modulos.menus import Menu_login
from modulos.clases_usuarios import Usuario, Administrador
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
        Administrador().interactuar_menu()
        