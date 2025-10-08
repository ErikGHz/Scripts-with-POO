import mysql.connector, os
from mysql.connector import Error

class BaseDeDatos:
    def __init__(self) -> None:
        self.host = os.environ['WORDPRESS_DB_HOST']
        self.user = os.environ['WORDPRESS_DB_USER']
        self.password = os.environ['WORDPRESS_DB_PASSWORD']
        self.db = None
        self.cursor = None

    def conectar_servidor(self) -> None:
        try:
            self.db = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password
            )
        except Error as err:
            if err.errno == 2003:
                print("No se ha podido conectar a la base de datos.")
        else:
            print("Conexion establecida a la base de datos correctamente.")
            self.cursor = self.db.cursor()


    def verificar_bd(self, base_datos) -> bool:
        base_datos = base_datos
        self.cursor.execute(f"SELECT IF(COUNT(*) > 0, 1, 0) FROM information_schema.schemata WHERE SCHEMA_NAME = '{base_datos}'")
        #Si la base de datos existe es 1 (TRUE), si no existe sera 0 (FALSE)
        for contenido in self.cursor:
            valor = bool(contenido[0])
        return valor
    
    def verificar_usuario(self, usuario) -> bool:
        usuario = usuario
        if self.db is not None and self.db.is_connected():
            self.cursor.execute(f"SELECT IF(COUNT(*) > 0, 1, 0) FROM mysql.user WHERE USER = '{usuario}'")
            #Si la base de datos existe es 1 (TRUE), si no existe sera 0 (FALSE)
            for contenido in self.cursor:
                valor = bool(contenido[0])
            return valor
        
    def verificar_recursos(self, base_datos) -> bool:
        base_datos = base_datos
        usuario = base_datos
        if not self.verificar_bd(base_datos) and not self.verificar_usuario(usuario):
            return True
        else: 
            print("Ya existe una base datos o un usuario con el mismo nombre.")
            return False

    def crear_bd(self, base_datos) -> None:
        base_datos = base_datos
        try:
            self.cursor.execute(f"CREATE DATABASE {base_datos};")
        except Error as err:
            if err.errno == 1007:
                print("La base de datos ya existe")

    #Usuario y Base De Datos tienen el mismo nombre.
    def crear_usuario(self, usuario, contrasena) -> None:
        usuario = usuario
        contrasena = contrasena
        try:
            self.cursor.execute(f"CREATE USER '{usuario}'@'%' IDENTIFIED BY '{contrasena}'")
        except Error as err:
            if err.errno == 1396:
                print("El usuario ya existe")
        else:
            self.cursor.execute(f"GRANT ALL PRIVILEGES ON {usuario}.* TO '{usuario}'@'%'")
            self.cursor.execute("FLUSH PRIVILEGES")
            
    def crear_recursos(self, base_datos, contrasena) -> bool:
        base_datos = base_datos
        contrasena = contrasena
        try:
            if self.verificar_recursos(base_datos):
                self.crear_bd(base_datos)
                self.crear_usuario(base_datos, contrasena)
                print("Base de datos creada correctamente.")
                return True
            else:
                print("No se ha creado nada.")
                return False
        except AttributeError:
            print("No se ha inicializado una conexion")
            return False

    def eliminar_bd(self, base_datos) -> None:
        if self.verificar_bd(base_datos) == True:
            self.cursor.execute(f"DROP DATABASE {base_datos};")
            print("La base de datos se borró correctamente")
        else:
            print("No existe la base de datos")

