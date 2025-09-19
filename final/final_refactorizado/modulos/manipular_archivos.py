import json  # Para manejar archivos JSON
import os    # Para trabajar con rutas y verificar existencia de archivos
from datetime import date

class Gestor_datos:
    def __init__(self, ruta_base=r'modulos\archivos'):
        self.__ruta_base = ruta_base  # Ruta donde se guardarán los archivos
        self.__archivo_usuarios = os.path.join(self.__ruta_base, 'usuarios.json')  # Ruta completa usuarios
        self.__archivo_admins = os.path.join(self.__ruta_base, 'administradores.json')  # Ruta completa admins
        self.__usuarios_borrados = os.path.join(self.__ruta_base, 'usuarios_borrados.json')
        self.verificar_o_crear_archivos()  # Asegura que los archivos existan

    def verificar_o_crear_archivos(self):
        os.makedirs(self.__ruta_base, exist_ok=True)  # Crea la carpeta si no existe

        # Crea archivo de usuarios si no existe
        if not os.path.exists(self.__archivo_usuarios):
            with open(self.__archivo_usuarios, 'w') as f:
                json.dump([], f)

        # Crea archivo de administradores si no existe
        if not os.path.exists(self.__archivo_admins):
            with open(self.__archivo_admins, 'w') as f:
                json.dump([], f)
        
        if not os.path.exists(self.__usuarios_borrados):
            with open(self.__usuarios_borrados, 'w') as f:
                json.dump([], f)

    def agregar_usuario(self, nombre, nombre_usuario, contraseña, veces_ingresadas=0, apis_visitadas=0, ultima_api_visitada = ""):
        nuevo_usuario = {
            "nombre": nombre,
            "nombre_usuario": nombre_usuario,
            "contraseña": contraseña,
            "veces_ingresadas": veces_ingresadas,
            "apis_visitadas": apis_visitadas,
            "ultima_api_visitada": ultima_api_visitada
        }
        try:
            with open(self.__archivo_usuarios, 'r+', encoding='utf-8') as f:
                datos = json.load(f)
                if self.verificar_nombre_usuario(self.__archivo_usuarios, nombre_usuario):
                    print(f"⚠️ El nombre de usuario '{nombre_usuario}' ya existe. No se agregó.")
                    return False
                datos.append(nuevo_usuario)
                f.seek(0)
                json.dump(datos, f, indent=4)
                f.truncate()
                print(f"✅ Usuario '{nombre_usuario}' agregado correctamente.")
                return True
        except Exception as e:
            print(f"❌ Error al agregar el usuario: {e}")

    def agregar_administrador(self, nombre_usuario, contraseña):
        nuevo_admin = {
            "nombre_usuario": nombre_usuario,
            "contraseña": contraseña
        }
        try:
            with open(self.__archivo_admins, 'r+', encoding='utf-8') as f:
                datos = json.load(f)
                if self.verificar_nombre_usuario(self.__archivo_admins, nombre_usuario):
                    print(f"⚠️ El administrador '{nombre_usuario}' ya existe. No se agregó.")
                    return
                datos.append(nuevo_admin)
                f.seek(0)
                json.dump(datos, f, indent=4)
                f.truncate()
                print(f"✅ Administrador '{nombre_usuario}' agregado correctamente.")
        except Exception as e:
            print(f"❌ Error al agregar el administrador: {e}")

    def actualizar_usuario(self, nombre_usuario, nuevas_visitas, nuevas_apis_visitadas, ultima_api_visitada):
        try:
            with open(self.__archivo_usuarios, 'r+', encoding='utf-8') as f:
                datos = json.load(f)
                usuario_encontrado = False

                for usuario in datos:
                    if usuario["nombre_usuario"] == nombre_usuario:
                        usuario["veces_ingresadas"] += nuevas_visitas
                        usuario["apis_visitadas"] += nuevas_apis_visitadas
                        usuario["ultima_api_visitada"] = ultima_api_visitada
                        usuario_encontrado = True
                        break

                if usuario_encontrado:
                    f.seek(0)
                    json.dump(datos, f, indent=4)
                    f.truncate()
                    print(f"✅ Usuario '{nombre_usuario}' actualizado correctamente.")
                else:
                    print(f"⚠️ Usuario '{nombre_usuario}' no encontrado.")
        except Exception as e:
            print(f"❌ Error al actualizar el usuario: {e}")
            
    def modificar_contraseña_usuario(self, nombre_usuario, nueva_contraseña):
        "Esta funcion modifica la contraseña del ususario"
        
        try:
            with open(self.__archivo_usuarios, 'r+', encoding='utf-8') as f:
                datos = json.load(f)
                usuario_encontrado = False

                for usuario in datos:
                    if usuario["nombre_usuario"] == nombre_usuario:
                        usuario["contraseña"] = nueva_contraseña
                        usuario_encontrado = True
                        break

                if usuario_encontrado:
                    f.seek(0)
                    json.dump(datos, f, indent=4)
                    f.truncate()
                    print(f"✅ Contraseña actualizada correctamente.")
                else:
                    print(f"⚠️ Usuario '{nombre_usuario}' no encontrado.")
        except Exception as e:
            print(f"❌ Error al actualizar el usuario: {e}")

    def borrar_usuario(self, nombre_usuario, motivo):
        """
        Elimina un usuario del archivo de usuarios y lo registra en usuarios_borrados.json
        con nombre, nombre_usuario, fecha (solo día), motivo, veces_ingresadas y apis_visitadas.
        """
        try:
            with open(self.__archivo_usuarios, 'r+', encoding='utf-8') as f_usuarios:
                usuarios = json.load(f_usuarios)
                usuario_encontrado = None

                # Buscar el usuario
                for usuario in usuarios:
                    if usuario["nombre_usuario"] == nombre_usuario:
                        usuario_encontrado = usuario
                        break

                if not usuario_encontrado:
                    print(f"⚠️ Usuario '{nombre_usuario}' no encontrado.")
                    return False

                # Eliminar del archivo original
                usuarios = [u for u in usuarios if u["nombre_usuario"] != nombre_usuario]
                f_usuarios.seek(0)
                json.dump(usuarios, f_usuarios, indent=4)
                f_usuarios.truncate()

            # Registrar en archivo de borrados
            usuario_borrado = {
                "nombre": usuario_encontrado["nombre"],
                "nombre_usuario": usuario_encontrado["nombre_usuario"],
                "fecha_borrado": date.today().isoformat(),  # Solo día
                "motivo": motivo,
                "veces_ingresadas": usuario_encontrado.get("veces_ingresadas", 0),
                "apis_visitadas": usuario_encontrado.get("apis_visitadas", 0),
                "ultima_api_visitada": usuario_encontrado.get("ultima_api_visitada", 0)
            }
            
            with open(self.__usuarios_borrados, 'r+', encoding='utf-8') as f_borrados:
                borrados = json.load(f_borrados)
                borrados.append(usuario_borrado)
                f_borrados.seek(0)
                json.dump(borrados, f_borrados, indent=4)
                f_borrados.truncate()
            return True

        except Exception as e:
            print(f"❌ Error al borrar el usuario: {e}")
            return False


    
    def verificar_nombre_usuario(self, ruta_archivo, nombre_usuario):
        """
        Verifica si el nombre_usuario existe en el archivo JSON especificado.
        Retorna True si existe, False si no.
        """
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                return any(item.get("nombre_usuario") == nombre_usuario for item in datos)
        except FileNotFoundError:
            print(f"⚠️ El archivo '{ruta_archivo}' no existe.")
            return False
        except json.JSONDecodeError:
            print(f"⚠️ El archivo '{ruta_archivo}' no contiene un JSON válido.")
            return False
        except Exception as e:
            print(f"❌ Error al verificar el nombre de usuario: {e}")
            return False
    
    def verificar_credenciales(self, ruta_archivo, nombre_usuario, contraseña):
        """
        Verifica si el nombre_usuario existe y si su contraseña coincide.
        Retorna True si ambos coinciden, False si no.
        """
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                for item in datos:
                    if item.get("nombre_usuario") == nombre_usuario:
                        return item.get("contraseña") == contraseña
                return False  # Usuario no encontrado
        except FileNotFoundError:
            print(f"⚠️ El archivo '{ruta_archivo}' no existe.")
            return False
        except json.JSONDecodeError:
            print(f"⚠️ El archivo '{ruta_archivo}' no contiene un JSON válido.")
            return False
        except Exception as e:
            print(f"❌ Error al verificar credenciales: {e}")
            return False
        
    def obtener_datos_usuarios(self):
        """
        Devuelve una lista de listas con los datos de los usuarios,
        lista que puede ser usada directamente con tabulate.
        """
        try:
            tabla = []

            # Usuarios activos
            with open(self.__archivo_usuarios, 'r', encoding='utf-8') as A:
                datos_activos = json.load(A)
                if not datos_activos:
                    print("⚠️ No hay usuarios activos registrados.")
                else:
                    for usuario_activo in datos_activos:
                        fila = [
                            usuario_activo.get("nombre", ""),
                            usuario_activo.get("nombre_usuario", ""),
                            usuario_activo.get("veces_ingresadas", 0),
                            usuario_activo.get("apis_visitadas", 0),
                            usuario_activo.get("ultima_api_visitada", "")
                        ]
                        tabla.append(fila)

            # Usuarios inactivos
            with open(self.__usuarios_borrados, "r", encoding='utf-8') as I:
                datos_inactivos = json.load(I)
                if not datos_inactivos:
                    print("⚠️ No hay usuarios inactivos registrados.")
                else:
                    for usuario_inactivo in datos_inactivos:
                        fila = [
                            usuario_inactivo.get("nombre", ""),
                            usuario_inactivo.get("nombre_usuario", ""),
                            usuario_inactivo.get("veces_ingresadas", 0),
                            usuario_inactivo.get("apis_visitadas", 0),
                            usuario_inactivo.get("ultima_api_visitada", "")
                        ]
                        tabla.append(fila)

            return tabla  # 👉 devolvemos los datos combinados

        except Exception as e:
            print(f"❌ Error al obtener los datos de usuarios: {e}")
            return []
    
    def obtener_datos_usuarios_activos(self):
        """
        Devuelve una lista de listas con los datos de los usuarios,
        lista que puede ser usada directamente con tabulate.
        """
        try:
            tabla = []

            # Usuarios activos
            with open(self.__archivo_usuarios, 'r', encoding='utf-8') as A:
                datos_activos = json.load(A)
                if not datos_activos:
                    print("⚠️ No hay usuarios activos registrados.")
                else:
                    for usuario_activo in datos_activos:
                        fila = [
                            usuario_activo.get("nombre", ""),
                            usuario_activo.get("nombre_usuario", ""),
                            usuario_activo.get("veces_ingresadas", 0),
                            usuario_activo.get("apis_visitadas", 0),
                            usuario_activo.get("ultima_api_visitada", "")
                        ]
                        tabla.append(fila)
            return tabla  # 👉 devolvemos los datos
        except Exception as e:
            print(f"❌ Error al obtener los datos de usuarios: {e}")
            return []
    
    def obtener_datos_usuarios_inactivos(self):
        try:
            tabla = []
            # Usuarios inactivos
            with open(self.__usuarios_borrados, "r", encoding='utf-8') as I:
                datos_inactivos = json.load(I)
                if not datos_inactivos:
                    print("⚠️ No hay usuarios inactivos registrados.")
                else:
                    for usuario_inactivo in datos_inactivos:
                        fila = [
                            usuario_inactivo.get("nombre", ""),
                            usuario_inactivo.get("nombre_usuario", ""),
                            usuario_inactivo.get("veces_ingresadas", 0),
                            usuario_inactivo.get("apis_visitadas", 0),
                            usuario_inactivo.get("ultima_api_visitada", "")
                        ]
                        tabla.append(fila)
            return tabla  # 👉 devolvemos los datos

        except Exception as e:
            print(f"❌ Error al obtener los datos de usuarios: {e}")
            return []