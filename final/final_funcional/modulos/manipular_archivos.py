import json  # Para manejar archivos JSON
import os    # Para trabajar con rutas y verificar existencia de archivos

class Gestor_datos:
    def __init__(self, ruta_base=r'modulos\archivos'):
        self.__ruta_base = ruta_base  # Ruta donde se guardarán los archivos
        self.__archivo_usuarios = os.path.join(self.__ruta_base, 'usuarios.json')  # Ruta completa usuarios
        self.__archivo_admins = os.path.join(self.__ruta_base, 'administradores.json')  # Ruta completa admins
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

    def agregar_usuario(self, nombre, nombre_usuario, contraseña, veces_ingresadas=0, cantidad_paginas_visitadas=0, ultima_pagina_visitada = ""):
        nuevo_usuario = {
            "nombre": nombre,
            "nombre_usuario": nombre_usuario,
            "contraseña": contraseña,
            "veces_ingresadas": veces_ingresadas,
            "cantidad_paginas_visitadas": cantidad_paginas_visitadas,
            "ultima_pagina_visitada": ultima_pagina_visitada
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

    def actualizar_usuario(self, nombre_usuario, nuevas_visitas, nuevas_paginas, ultima_pagina_visitada):
        try:
            with open(self.__archivo_usuarios, 'r+', encoding='utf-8') as f:
                datos = json.load(f)
                usuario_encontrado = False

                for usuario in datos:
                    if usuario["nombre_usuario"] == nombre_usuario:
                        usuario["veces_ingresadas"] += nuevas_visitas
                        usuario["cantidad_paginas_visitadas"] += nuevas_paginas
                        usuario["ultima_pagina_visitada"] = ultima_pagina_visitada
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
            with open(self.__archivo_usuarios, 'r', encoding='utf-8') as f:
                datos = json.load(f)

                # Si no hay usuarios, devuelve una lista vacía
                if not datos:
                    print("⚠️ No hay usuarios registrados.")
                    return []

                # Extrae los campos relevantes para la tabla
                tabla = []
                for usuario in datos:
                    fila = [
                        usuario.get("nombre", ""),
                        usuario.get("nombre_usuario", ""),
                        usuario.get("veces_ingresadas", 0),
                        usuario.get("cantidad_paginas_visitadas", 0),
                        usuario.get("ultima_pagina_visitada", "")
                    ]
                    tabla.append(fila)

                return tabla

        except Exception as e:
            print(f"❌ Error al obtener los datos de usuarios: {e}")
            return []

    def filtrar_datos_varios(self, campo, valor_buscado):
        """
        Devuelve una lista de usuarios donde el campo coincide con el valor buscado.
        """
        try:
            with open(self.__archivo_usuarios, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                filtrados = [
                    d for d in datos
                    if str(d.get(campo, "")).lower() == str(valor_buscado).lower()
                ]
                return filtrados
        except Exception as e:
            print(f"❌ Error al filtrar datos: {e}")
            return []

    def mostrar_valores(self, campo):
        """
        Devuelve los valores para que sea mas facil realizar la busqueda
        """
        try:
            with open(self.__archivo_usuarios, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                valores = [
                    d for d in datos
                    if str(d.get(campo, "")).lower()
                ]
                return valores
        except Exception as e:
            print(f"❌ Error al filtrar datos: {e}")
            return []    
    