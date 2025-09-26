import string, mysql.connector, os, time

class BasedeDatos:
    def __init__(self) -> None:
        self.host = "localhost"
        self.user = "root"
        self.password = "root"
        self.db = None
        self.cursor = None

    def conectar_servidor(self) -> None:
        self.db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password
        )
        if self.db.is_connected():
            print(f"Conectado correctamente a {self.host}")
            self.cursor = self.db.cursor()
        else:
            print(f"No se ha podido conectar {self.host}")
    
    def verificar_bd(self, nombre) -> bool:
        if self.db is None or not self.db.is_connected():
            print("No te has conectado a una base de datos")
            return False
        
        else:
            #Si la base de datos existe es 1, si no existe sera 0
            self.cursor.execute(f"SELECT IF(COUNT(*) > 0, 1, 0) FROM information_schema.schemata WHERE SCHEMA_NAME = '{nombre}'")
            for verify in self.cursor:
                print(verify[0])
                return bool(verify[0])
            
    def crear_bd(self, nombre) -> None:
        nombre = nombre
        self.conectar_servidor()
        self.verificar_bd(nombre)
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre};")

    def eliminar_bd(self, nombre) -> None:
        nombre = nombre
        self.conectar_servidor()
        if self.verificar_bd(nombre) == True:
            self.cursor.execute(f"DROP DATABASE {nombre};")
            print("La base de datos se borró correctamente")
        else:
            print("No existe la base de datos")

    # def mostrar_bd(self) -> None:
    #     self.conectar_servidor()
    #     self.cursor.execute("SHOW DATABASES;")
    #     for mostrar in self.cursor:
    #         print(mostrar[0])
    
    def generarContraseña(self) -> None:
        letras = string.ascii_letters
        numeros = string.digits


bd = BasedeDatos()
bd.crear_bd("ERIK")