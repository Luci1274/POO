from modulos.manipular_archivos import Gestor_datos


class Login:
    """
    Clase de autenticación para usuarios y administradores.
    
    Diseñada para ser utilizada con Flask: no realiza ninguna interacción con consola (input/print).
    Las validaciones y el manejo de intentos se delegan a las rutas y sesiones de Flask.
    """

    def __init__(self):
        """Inicializa la clase con una instancia del gestor de datos."""
        self.gestor = Gestor_datos()

    def verificar_credenciales(self, nombre_usuario, contraseña):
        """
        Verifica las credenciales de un usuario tanto en la base de datos de usuarios como de administradores.

        Args:
            nombre_usuario (str): Nombre de usuario a verificar.
            contraseña (str): Contraseña a verificar.

        Returns:
            dict: Un diccionario con estructura {'ok': bool, 'tipo': str, 'usuario': str}
                  - 'ok': True si las credenciales son válidas, False en caso contrario.
                  - 'tipo': 'administrador' o 'usuario' si ok es True, None si es False.
                  - 'usuario': nombre del usuario si ok es True, None si es False.

        Raises:
            ValueError: Si los campos están vacíos.
        """
        # Validar que los campos no estén vacíos
        if not nombre_usuario or not contraseña:
            raise ValueError("El usuario y la contraseña no pueden estar vacíos.")

        # Caso especial: usuario maestro para administrador (credenciales hardcodeadas)
        if nombre_usuario == "...." and contraseña == "fe":
            return {
                "ok": True,
                "tipo": "administrador",
                "usuario": nombre_usuario
            }

        # Verificar si es un administrador válido
        if self._verificar_admin(nombre_usuario, contraseña):
            return {
                "ok": True,
                "tipo": "administrador",
                "usuario": nombre_usuario
            }

        # Verificar si es un usuario válido
        if self._verificar_usuario(nombre_usuario, contraseña):
            return {
                "ok": True,
                "tipo": "usuario",
                "usuario": nombre_usuario
            }

        # Credenciales inválidas
        return {
            "ok": False,
            "tipo": None,
            "usuario": None
        }

    def _verificar_usuario(self, nombre_usuario, contraseña):
        """
        Verifica las credenciales contra la base de datos de usuarios.

        Args:
            nombre_usuario (str): Nombre de usuario.
            contraseña (str): Contraseña del usuario.

        Returns:
            bool: True si las credenciales son válidas, False en caso contrario.
        """
        ruta_usuario = "modulos\\archivos\\usuarios.json"
        return self.gestor.verificar_credenciales(ruta_usuario, nombre_usuario, contraseña)

    def _verificar_admin(self, nombre_usuario, contraseña):
        """
        Verifica las credenciales contra la base de datos de administradores.

        Args:
            nombre_usuario (str): Nombre de usuario administrador.
            contraseña (str): Contraseña del administrador.

        Returns:
            bool: True si las credenciales son válidas, False en caso contrario.
        """
        ruta_admin = "modulos\\archivos\\administradores.json"
        return self.gestor.verificar_credenciales(ruta_admin, nombre_usuario, contraseña)

    def registrar_usuario(self, nombre, nombre_usuario, contraseña):
        """
        Registra un nuevo usuario en la base de datos.

        Args:
            nombre (str): Nombre real del usuario.
            nombre_usuario (str): Nombre de usuario único.
            contraseña (str): Contraseña del usuario.

        Returns:
            dict: {'ok': bool, 'mensaje': str}

        Raises:
            ValueError: Si alguno de los campos está vacío.
        """
        # Validar que ninguno de los campos esté vacío
        if not nombre or not nombre_usuario or not contraseña:
            raise ValueError("Todos los campos (nombre, usuario, contraseña) son obligatorios.")

        # Intentar añadir el usuario a través del gestor de datos
        resultado = self.gestor.agregar_usuario(nombre, nombre_usuario, contraseña)

        # Devolver un diccionario indicando el resultado
        if resultado:
            return {
                "ok": True,
                "mensaje": f"Usuario '{nombre_usuario}' registrado exitosamente."
            }
        else:
            return {
                "ok": False,
                "mensaje": "El usuario ya existe o hubo un error al registrarlo."
            }

    def cambiar_contraseña(self, nombre_usuario, nueva_contraseña):
        """
        Cambia la contraseña de un usuario existente.

        Args:
            nombre_usuario (str): Nombre del usuario cuya contraseña se va a cambiar.
            nueva_contraseña (str): La nueva contraseña.

        Returns:
            dict: {'ok': bool, 'mensaje': str}

        Raises:
            ValueError: Si el nombre de usuario o la contraseña están vacíos.
        """
        # Validar que los campos no estén vacíos
        if not nombre_usuario or not nueva_contraseña:
            raise ValueError("El usuario y la nueva contraseña no pueden estar vacíos.")

        # Llamar al método del gestor para modificar la contraseña
        resultado = self.gestor.modificar_contraseña_usuario(nombre_usuario, nueva_contraseña)

        # Devolver el resultado
        if resultado:
            return {
                "ok": True,
                "mensaje": f"Contraseña del usuario '{nombre_usuario}' actualizada exitosamente."
            }
        else:
            return {
                "ok": False,
                "mensaje": "No se pudo actualizar la contraseña. Verifica el usuario."
            }
