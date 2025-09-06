from modulos.menus import Menu_login

from typing import Optional

class Persona:
    def __init__(self):
        self.__nombre_usuario: Optional[str] = None
        self.tipo: Optional[str] = None
        self.menu_login = Menu_login()
        self.interactuar_login()
        
    def interactuar_login(self):
        resultado = self.menu_login.ejecutar()
        if resultado is not None:
            nombre_usuario = resultado[0]
            self.tipo = resultado[1]
            self.setter_nombre_usuario(nombre_usuario)
    
    def get_nombre_usuario(self):
        return self.__nombre_usuario
    
    def setter_nombre_usuario(self, nombre_usuario):
        self.__nombre_usuario = nombre_usuario