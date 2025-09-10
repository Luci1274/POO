from modulos.menus import Menu_usuario
from modulos.manipular_archivos import Gestor_datos

class Usuario:
    def __init__(self, nombre_usuario):
        self.__Nombre_usuario = nombre_usuario
        self.nuevas_visitas = int("")
        self.nuevas_paginas = int("")
        self.ultima_pagina_visitada = ""
        self.menu = Menu_usuario()
        self.interactuar_menu()    
    
    
    def get_nombre_usuario(self):
        return self.__Nombre_usuario
    
    def interactuar_menu():
        datos = self.menu()
        self.nuevas_visitas = datos[0]
        self.neuvas_paginas = datos[1]
        self.ultima_pagina_visitada = datos[2]
        if self.ultima_pagina_visitada == None or self.ultima_pagina_visitada == True:
            self.ultima_pagina_visitada = "ninguna"
        else:
            pass
        
    def actualizar_informacion(self):
        nombre_usuario = get_nombre_usuario()
        Gestor_datos().actualizar_usuario(nombre_usuario, self.nuevas_visitas, self.nuevas_paginas, self.ultima_pagina_visitada)

