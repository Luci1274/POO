from modulos.menus import Menu_usuario
from modulos.manipular_archivos import Gestor_datos

class Usuario:
    def __init__(self, nombre_usuario):
        self.__Nombre_usuario = nombre_usuario
        self.nuevas_visitas = 0
        self.apis_visitadas = 0
        self.ultima_api_visitada = ""
        self.menu = Menu_usuario()
    
    
    def get_nombre_usuario(self):
        return self.__Nombre_usuario
    
    def interactuar_menu(self):
        datos = self.menu.ejecutar()
        self.nuevas_visitas = datos[0]
        self.apis_visitadas = datos[1]
        self.ultima_api_visitada = datos[2]
        eliminar = datos[3]
        if self.ultima_api_visitada == None or self.ultima_api_visitada == True:
            self.ultima_api_visitada = "ninguna"
        else:
            int(self.nuevas_visitas)
            int(self.apis_visitadas)
            str(self.ultima_api_visitada)
        return eliminar
    
    def eliminar_cuenta(self):
        nombre_usuario = self.get_nombre_usuario()
        Gestor_datos().actualizar_usuario(nombre_usuario, self.nuevas_visitas, self.apis_visitadas, self.ultima_api_visitada)
        Gestor_datos().borrar_usuario(nombre_usuario, "Decision propia y voluntaria")
    
    def actualizar_informacion(self):
        nombre_usuario = self.get_nombre_usuario()
        Gestor_datos().actualizar_usuario(nombre_usuario, self.nuevas_visitas, self.apis_visitadas, self.ultima_api_visitada)

