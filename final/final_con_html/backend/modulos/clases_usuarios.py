from modulos.menus import Menu_usuario, Menu_administrador
from modulos.manipular_archivos import Gestor_datos

class Usuario:
    """Clase que representa a un usuario del sistema"""
    def __init__(self, nombre_usuario):
        self.__Nombre_usuario = nombre_usuario
        self.nuevas_visitas = 0
        self.apis_visitadas = 0
        self.ultima_api_visitada = ""
        self.menu = Menu_usuario()
    
    
    def get_nombre_usuario(self):
        """Devuelve el nombre de usuario"""
        return self.__Nombre_usuario
    
    def interactuar_menu(self):
        """Interactúa con el menú de usuario y actualiza los datos del usuario"""
        datos = self.menu.ejecutar()
        self.nuevas_visitas = datos[0]
        self.apis_visitadas = datos[1]
        self.ultima_api_visitada = datos[2]
        eliminar = datos[3]
        consultas_api = datos[4]
        if self.ultima_api_visitada == None or self.ultima_api_visitada == True:
            self.ultima_api_visitada = "ninguna"
        else:
            int(self.nuevas_visitas)
            int(self.apis_visitadas)
            str(self.ultima_api_visitada)
        Gestor_datos().actualizar_consultas_api(consultas_api)
        return eliminar
    
    def eliminar_cuenta(self):
        """Elimina la cuenta del usuario y actualiza los datos"""
        nombre_usuario = self.get_nombre_usuario()
        Gestor_datos().actualizar_usuario(nombre_usuario, self.nuevas_visitas, self.apis_visitadas, self.ultima_api_visitada)
        Gestor_datos().borrar_usuario(nombre_usuario, "Decision propia y voluntaria")
    
    def actualizar_informacion(self):
        """Actualiza la información del usuario en el archivo de datos"""
        nombre_usuario = self.get_nombre_usuario()
        Gestor_datos().actualizar_usuario(nombre_usuario, self.nuevas_visitas, self.apis_visitadas, self.ultima_api_visitada)

class Administrador():
    def __init__ (self):
        self.menu_ad = Menu_administrador()

    def interactuar_menu(self):
        """Interactúa con el menú de administrador"""
        self.menu_ad.ejecutar()
        