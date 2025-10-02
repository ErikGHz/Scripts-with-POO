import mysql.connector
from mysql.connector import Error

class BaseDeDatos:
    def __init__(self) -> None:
        self.host = "db-app"
        self.user = "root"
        self.password = "root"
        self.db = None
        self.cursor = None

    def conectarServidor(self) -> None:
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


    def verificarBD(self, baseDatos) -> bool:
        self.cursor.execute(f"SELECT IF(COUNT(*) > 0, 1, 0) FROM information_schema.schemata WHERE SCHEMA_NAME = '{baseDatos}'")
        #Si la base de datos existe es 1 (TRUE), si no existe sera 0 (FALSE)
        for contenido in self.cursor:
            valor = bool(contenido[0])
        return valor
    
    def verificarUsuario(self, usuario) -> bool:
        if self.db is not None and self.db.is_connected():
            self.cursor.execute(f"SELECT IF(COUNT(*) > 0, 1, 0) FROM mysql.user WHERE USER = '{usuario}'")
            #Si la base de datos existe es 1 (TRUE), si no existe sera 0 (FALSE)
            for contenido in self.cursor:
                valor = bool(contenido[0])
            return valor
        
    def verificarRecursos(self, baseDatos) -> bool:
        if not self.verificarBD(baseDatos) and not self.verificarUsuario(baseDatos):
            return True
        else: 
            print("Ya existe una base datos o un usuario con el mismo nombre.")
            return False

    def crearBD(self, baseDatos) -> None:
        try:
            self.cursor.execute(f"CREATE DATABASE {baseDatos};")
        except Error as err:
            if err.errno == 1007:
                print("La base de datos ya existe")

    #Usuario y Base De Datos tienen el mismo nombre.
    def crearUsuario(self, usuario, contraseña) -> None:
        try:
            self.cursor.execute(f"CREATE USER '{usuario}'@'%' IDENTIFIED BY '{contraseña}'")
        except Error as err:
            if err.errno == 1396:
                print("El usuario ya existe")
        else:
            self.cursor.execute(f"GRANT ALL PRIVILEGES ON {usuario}.* TO '{usuario}'@'%'")


    def crearRecursos(self, baseDatos, contraseña) -> bool:
        try:
            if self.verificarRecursos(baseDatos):
                self.crearBD(baseDatos)
                self.crearUsuario(baseDatos, contraseña)
                print("Base de datos creada correctamente.")
                return True
            else:
                print("No se ha creado nada.")
                return False
        except AttributeError:
            print("No se ha inicializado una conexion")
            return False
            
    

    def eliminarBD(self, baseDatos) -> None:
        if self.verificarBD(baseDatos) == True:
            self.cursor.execute(f"DROP DATABASE {baseDatos};")
            print("La base de datos se borró correctamente")
        else:
            print("No existe la base de datos")