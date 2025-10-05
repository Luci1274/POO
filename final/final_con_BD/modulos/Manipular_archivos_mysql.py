import mysql.connector
from datetime import date

class Gestor_datos:
    def __init__(self, host='localhost', user='root', password='1274', database='poo_final'):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        # Tabla usuarios
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            nombre_usuario VARCHAR(100) UNIQUE,
            contraseña VARCHAR(100),
            veces_ingresadas INT DEFAULT 0,
            apis_visitadas INT DEFAULT 0,
            ultima_api_visitada VARCHAR(255)
        )
        """)
        # Tabla administradores
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS administradores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre_usuario VARCHAR(100) UNIQUE,
            contraseña VARCHAR(100)
        )
        """)
        # Tabla usuarios borrados
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios_borrados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            nombre_usuario VARCHAR(100),
            fecha_borrado DATE,
            motivo VARCHAR(255),
            veces_ingresadas INT,
            apis_visitadas INT,
            ultima_api_visitada VARCHAR(255)
        )
        """)
        # Tabla consultas api
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultas_api (
            id INT AUTO_INCREMENT PRIMARY KEY,
            api_nombre VARCHAR(100),
            veces_consultada INT DEFAULT 0
        )
        """)
        self.conn.commit()

    def agregar_usuario(self, nombre, nombre_usuario, contraseña, veces_ingresadas=0, apis_visitadas=0, ultima_api_visitada=""):
        try:
            self.cursor.execute("""
                INSERT INTO usuarios (nombre, nombre_usuario, contraseña, veces_ingresadas, apis_visitadas, ultima_api_visitada)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (nombre, nombre_usuario, contraseña, veces_ingresadas, apis_visitadas, ultima_api_visitada))
            self.conn.commit()
            print(f"✅ Usuario '{nombre_usuario}' agregado correctamente.")
            return True
        except mysql.connector.IntegrityError:
            print(f"⚠️ El nombre de usuario '{nombre_usuario}' ya existe. No se agregó.")
            return False

    def actualizar_usuario(self, nombre_usuario, nuevas_visitas, nuevas_apis_visitadas, ultima_api_visitada):
        self.cursor.execute("""
            UPDATE usuarios
            SET veces_ingresadas = veces_ingresadas + %s,
                apis_visitadas = apis_visitadas + %s,
                ultima_api_visitada = %s
            WHERE nombre_usuario = %s
        """, (nuevas_visitas, nuevas_apis_visitadas, ultima_api_visitada, nombre_usuario))
        self.conn.commit()
        print(f"✅ Usuario '{nombre_usuario}' actualizado correctamente.")

    def modificar_contraseña_usuario(self, nombre_usuario, nueva_contraseña):
        self.cursor.execute("""
            UPDATE usuarios
            SET contraseña = %s
            WHERE nombre_usuario = %s
        """, (nueva_contraseña, nombre_usuario))
        self.conn.commit()
        print(f"✅ Contraseña actualizada correctamente.")

    def verificar_nombre_usuario(self, nombre_usuario):
        self.cursor.execute("""
            SELECT 1 FROM usuarios WHERE nombre_usuario = %s
        """, (nombre_usuario,))
        return self.cursor.fetchone() is not None

    def verificar_credenciales(self, nombre_usuario, contraseña):
        self.cursor.execute("""
            SELECT 1 FROM usuarios WHERE nombre_usuario = %s AND contraseña = %s
        """, (nombre_usuario, contraseña))
        return self.cursor.fetchone() is not None

    def obtener_datos_usuarios(self):
        self.cursor.execute("""
            SELECT nombre, nombre_usuario, veces_ingresadas, apis_visitadas, ultima_api_visitada FROM usuarios
        """)
        return self.cursor.fetchall()

    # Métodos para administradores
    def agregar_administrador(self, nombre_usuario, contraseña):
        try:
            self.cursor.execute("""
                INSERT INTO administradores (nombre_usuario, contraseña)
                VALUES (%s, %s)
            """, (nombre_usuario, contraseña))
            self.conn.commit()
            print(f"✅ Administrador '{nombre_usuario}' agregado correctamente.")
            return True
        except mysql.connector.IntegrityError:
            print(f"⚠️ El administrador '{nombre_usuario}' ya existe.")
            return False

    def verificar_admin(self, nombre_usuario, contraseña):
        self.cursor.execute("""
            SELECT 1 FROM administradores WHERE nombre_usuario = %s AND contraseña = %s
        """, (nombre_usuario, contraseña))
        return self.cursor.fetchone() is not None

    # Métodos para usuarios borrados
    def borrar_usuario(self, nombre, nombre_usuario, motivo, veces_ingresadas, apis_visitadas, ultima_api_visitada):
        self.cursor.execute("""
            INSERT INTO usuarios_borrados (nombre, nombre_usuario, fecha_borrado, motivo, veces_ingresadas, apis_visitadas, ultima_api_visitada)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nombre, nombre_usuario, date.today(), motivo, veces_ingresadas, apis_visitadas, ultima_api_visitada))
        self.conn.commit()
        print(f"✅ Usuario '{nombre_usuario}' borrado y registrado en usuarios_borrados.")

    def obtener_usuarios_borrados(self):
        self.cursor.execute("""
            SELECT nombre, nombre_usuario, fecha_borrado, motivo, veces_ingresadas, apis_visitadas, ultima_api_visitada FROM usuarios_borrados
        """)
        return self.cursor.fetchall()

    # Métodos para consultas API
    def actualizar_consultas_api(self, api_nombre):
        # Si existe, suma 1; si no, lo crea
        self.cursor.execute("""
            SELECT veces_consultada FROM consultas_api WHERE api_nombre = %s
        """, (api_nombre,))
        resultado = self.cursor.fetchone()
        if resultado:
            self.cursor.execute("""
                UPDATE consultas_api SET veces_consultada = veces_consultada + 1 WHERE api_nombre = %s
            """, (api_nombre,))
        else:
            self.cursor.execute("""
                INSERT INTO consultas_api (api_nombre, veces_consultada) VALUES (%s, 1)
            """, (api_nombre,))
        self.conn.commit()

    def obtener_consultas_api(self):
        self.cursor.execute("""
            SELECT api_nombre, veces_consultada FROM consultas_api
        """)
        return self.cursor.fetchall()