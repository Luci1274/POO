from manipular_archivos import GestorDatos

class Login:
    def __init__(self):
        self.gestor = GestorDatos()
    
    def ingresar_usuario(self):
        while True:
            print("Para iniciar sesion por favor ingrese el nombre de usuario y contraseña")
            nombre_usuario = input("Por favor ingrese su nombre de usuario: ").strip()
            contraseña = input("Por favor ingrese su contraseña: ").strip()
            if len(nombre_usuario) == 0 or len(contraseña) == 0:
                print("Por favor rellene los campos")
                continue
            elif self.verificar_usuario(nombre_usuario, contraseña) == True: 
                self.gestor.actualizar_usuario(nombre_usuario, 1, 0)
                print("Inicio exitoso")
                break
            elif self.verificar_admin(nombre_usuario, contraseña) == True: 
                print("Inicio exitoso bienvenido señor")
                break
            else:
                print("Usuario o contraseña inocrrecta, por favor intente nuevamente")
                continue
            

    def verificar_usuario(self, nombre_usuario, contraseña):
        ruta_usuario = "modulos\archivos\usuarios.json" 
        self.gestor.verificar_credenciales(ruta_usuario, nombre_usuario, contraseña)
        return

    def verificar_admin(self, nombre_usuario, contraseña):
        ruta_admin = "modulos\archivos\administradores.json" 
        self.gestor.verificar_credenciales(ruta_admin, nombre_usuario, contraseña)
        return

    def registrar_usuario(self):
        while True:
            print("Por favor llene los siguientes espacios para crear un usuario")
            nombre = input("Por favor ingrese su nombre de real: ").strip()
            nombre_usuario = input("Por favor ingrese su nombre de usuario: ")
            contraseña = input("Por favor ingrese su contraseña: ").strip()
            if len(nombre_usuario) == 0 or len(contraseña) == 0 or len(nombre) == 0:
                print("Por favor rellene los campos")
                continue
            elif self.gestor.agregar_usuario(nombre, nombre_usuario, contraseña) == True:
                self.usuario = Usuario(nombre, nombre_usuario, contraseña)
                break
            else:
                continue

        

class Usuario:
    def __init__(self, nombre, nombre_usuario, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        self.nombre_usuario = nombre_usuario
