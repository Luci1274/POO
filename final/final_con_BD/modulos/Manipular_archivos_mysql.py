import mysql.connector
from datetime import date

class Gestor_datos:
    def __init__(self, host='localhost', user='root', password='1274', database='Programacion_final'):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.inicializar_tablas()

    def inicializar_tablas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100),
                nombre_usuario VARCHAR(50) UNIQUE,
                contraseña VARCHAR(100),
                veces_ingresadas INT DEFAULT 0,
                apis_visitadas INT DEFAULT 0,
                ultima_api_visitada TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS administradores (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre_usuario VARCHAR(50) UNIQUE,
                contraseña VARCHAR(100)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios_borrados (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100),
                nombre_usuario VARCHAR(50),
                fecha_borrado DATE,
                motivo TEXT,
                veces_ingresadas INT,
                apis_visitadas INT,
                ultima_api_visitada TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS consultas_api (
                id INT AUTO_INCREMENT PRIMARY KEY,
                api VARCHAR(255) UNIQUE,
                veces_consultada INT DEFAULT 0
            )
        """)
        self.conn.commit()
        
    def agregar_usuario(self, nombre, nombre_usuario, contraseña, veces_ingresadas=0, apis_visitadas=0, ultima_api_visitada=""):
        if self.verificar_nombre_usuario(nombre_usuario, tabla="usuarios"):
            print(f"⚠️ El nombre de usuario '{nombre_usuario}' ya existe.")
            return False
        self.cursor.execute("""
            INSERT INTO usuarios (nombre, nombre_usuario, contraseña, veces_ingresadas, apis_visitadas, ultima_api_visitada)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nombre, nombre_usuario, contraseña, veces_ingresadas, apis_visitadas, ultima_api_visitada))
        self.conn.commit()
        print(f"✅ Usuario '{nombre_usuario}' agregado correctamente.")
        return True

    def verificar_nombre_usuario(self, nombre_usuario, tabla="usuarios"):
        self.cursor.execute(f"SELECT 1 FROM {tabla} WHERE nombre_usuario = %s", (nombre_usuario,))
        return self.cursor.fetchone() is not None

    def actualizar_usuario(self, nombre_usuario, nuevas_visitas, nuevas_apis_visitadas, ultima_api_visitada):
        self.cursor.execute("""
            UPDATE usuarios
            SET veces_ingresadas = veces_ingresadas + %s,
                apis_visitadas = apis_visitadas + %s,
                ultima_api_visitada = %s
            WHERE nombre_usuario = %s
        """, (nuevas_visitas, nuevas_apis_visitadas, ultima_api_visitada, nombre_usuario))
        self.conn.commit()
        if self.cursor.rowcount:
            print(f"✅ Usuario '{nombre_usuario}' actualizado correctamente.")
        else:
            print(f"⚠️ Usuario '{nombre_usuario}' no encontrado.")

    def modificar_contraseña_usuario(self, nombre_usuario, nueva_contraseña):
        self.cursor.execute("""
            UPDATE usuarios SET contraseña = %s WHERE nombre_usuario = %s
        """, (nueva_contraseña, nombre_usuario))
        self.conn.commit()
        if self.cursor.rowcount:
            print("✅ Contraseña actualizada correctamente.")
        else:
            print(f"⚠️ Usuario '{nombre_usuario}' no encontrado.")

    def borrar_usuario(self, nombre_usuario, motivo):
        self.cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = %s", (nombre_usuario,))
        usuario = self.cursor.fetchone()
        if not usuario:
            print(f"⚠️ Usuario '{nombre_usuario}' no encontrado.")
            return False

        self.cursor.execute("DELETE FROM usuarios WHERE nombre_usuario = %s", (nombre_usuario,))
        self.cursor.execute("""
            INSERT INTO usuarios_borrados (nombre, nombre_usuario, fecha_borrado, motivo, veces_ingresadas, apis_visitadas, ultima_api_visitada)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            usuario["nombre"], usuario["nombre_usuario"], date.today(),
            motivo, usuario["veces_ingresadas"], usuario["apis_visitadas"], usuario["ultima_api_visitada"]
        ))
        self.conn.commit()
        print(f"✅ Usuario '{nombre_usuario}' borrado y registrado.")
        return True
    
    def actualizar_consultas_api(self, diccionario_consultas):
        for api, cantidad in diccionario_consultas.items():
            self.cursor.execute("SELECT * FROM consultas_api WHERE api = %s", (api,))
            resultado = self.cursor.fetchone()
            if resultado:
                self.cursor.execute("""
                    UPDATE consultas_api SET veces_consultada = veces_consultada + %s WHERE api = %s
                """, (cantidad, api))
            else:
                self.cursor.execute("""
                    INSERT INTO consultas_api (api, veces_consultada) VALUES (%s, %s)
                """, (api, cantidad))
        self.conn.commit()
        print("📦 Consultas a APIs actualizadas correctamente.")
        

    def verificar_credenciales(self, tabla, nombre_usuario, contraseña):
        self.cursor.execute(f"""
            SELECT contraseña FROM {tabla} WHERE nombre_usuario = %s
        """, (nombre_usuario,))
        resultado = self.cursor.fetchone()
        return resultado and resultado["contraseña"] == contraseña
    
    def obtener_datos_usuarios(self):
        return self.obtener_datos_usuarios_activos() + self.obtener_datos_usuarios_inactivos()

    def obtener_datos_usuarios_activos(self):
        self.cursor.execute("""
            SELECT nombre, nombre_usuario, veces_ingresadas, apis_visitadas, ultima_api_visitada FROM usuarios
        """)
        return [
            [u["nombre"], u["nombre_usuario"], u["veces_ingresadas"], u["apis_visitadas"], u["ultima_api_visitada"]]
            for u in self.cursor.fetchall()
        ]

    def obtener_datos_usuarios_inactivos(self):
        self.cursor.execute("""
            SELECT nombre, nombre_usuario, veces_ingresadas, apis_visitadas, ultima_api_visitada FROM usuarios_borrados
        """)
        return [
            [u["nombre"], u["nombre_usuario"], u["veces_ingresadas"], u["apis_visitadas"], u["ultima_api_visitada"]]
            for u in self.cursor.fetchall()
        ]

    def obtener_consultas_apis(self):
        self.cursor.execute("SELECT api, veces_consultada FROM consultas_api")
        return [
            [fila["api"], fila["veces_consultada"]] for fila in self.cursor.fetchall()
        ]