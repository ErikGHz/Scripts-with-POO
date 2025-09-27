import string, mysql.connector, os, time
from mysql.connector import Error

class BasedeDatos:
    def __init__(self) -> None:
        self.host = "localhost"
        self.user = "root"
        self.password = "root"
        self.db = None
        self.cursor = None

    def conectarServidor(self) -> None:
        self.db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password
        )
        if self.db is not None and self.db.is_connected():
            print(f"Conectado correctamente a {self.host}")
            self.cursor = self.db.cursor()
        else:
            print("La conexión con la base de datos no está activa.")
            
    def verificarBD(self, baseDatos) -> bool:
        if self.db is not None and self.db.is_connected():
            self.cursor.execute(f"SELECT IF(COUNT(*) > 0, 1, 0) FROM information_schema.schemata WHERE SCHEMA_NAME = '{baseDatos}'")
            #Si la base de datos existe es 1 (TRUE), si no existe sera 0 (FALSE)
            for contenido in self.cursor:
                valor = bool(contenido[0])
            return valor
        else:
            print("No te has conectado a una base de datos")
            return None
            
    def verificarUsuario(self, usuario) -> bool:
        if self.db is not None and self.db.is_connected():
            self.cursor.execute(f"SELECT IF(COUNT(*) > 0, 1, 0) FROM MYSQL.USER WHERE USER = '{usuario}'")\
            #Si la base de datos existe es 1 (TRUE), si no existe sera 0 (FALSE)
            for contenido in self.cursor:
                valor = bool(contenido[0])
            return valor
        else:
            print("No te has conectado a una base de datos")
            return None

    def crearBD(self, baseDatos) -> None:
        self.conectarServidor()
        self.verificarBD(baseDatos)
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {baseDatos};")

    def crearUsuario(self, usuario, contraseña) -> None:
        self.conectarServidor()
        self.verificarUsuario(usuario)
        self.cursor.execute(f"CREATE USER '{usuario}'@'%' IDENTIFIED BY '{contraseña}'")
                            
    def eliminarBD(self, baseDatos) -> None:
        self.conectarServidor()
        if self.verificarBD(baseDatos) == True:
            self.cursor.execute(f"DROP DATABASE {baseDatos};")
            print("La base de datos se borró correctamente")
        else:
            print("No existe la base de datos")

    # def mostrar_bd(self) -> None:
    #     self.conectar_servidor()
    #     self.cursor.execute("SHOW DATABASES;")
    #     for mostrar in self.cursor:
    #         print(mostrar[0])
    1
    def generarContraseña(self) -> None:
        letras = string.ascii_letters
        numeros = string.digits

bd = BasedeDatos()
bd.conectarServidor()
bd.verificarBD("erik")