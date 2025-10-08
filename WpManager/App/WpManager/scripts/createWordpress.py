import subprocess, os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Wordpress:
    def __init__(self, titulo, usuario, correo):
        self.titulo = titulo
        self.usuario = usuario
        self.contrasena = ""
        self.correo = correo

    def crear_directorio(self):
        nombre_directorio = self.titulo
        subprocess.run(["ls"])
        sh_comando = f"sh {BASE_DIR}/scripts/createwordpress.sh crear_directorio {nombre_directorio}"
        subprocess.run(sh_comando, shell=True)

    def copiar_docker(self):
        nombre_directorio = self.titulo
        sh_comando = f"sh {BASE_DIR}/scripts/createwordpress.sh copiar_docker {nombre_directorio}"
        subprocess.run(sh_comando, shell=True)

    def reemplazar_docker(self):
        nombre_servicio = self.titulo
        nombre_contenedor = self.titulo
        #Abre el archivo docker-compose.yaml y define un diccionario de variables
        with open(f'../wordpress/{self.titulo}/docker-compose.yaml', 'r') as file:
            archivo_docker = file.read()
            variables = {
            '$SERVICE_NAME': nombre_servicio,
            '$CONTAINER_NAME': nombre_contenedor,
            }
        #Sustituye las variables del diccionario
        for key, value in variables.items():
            archivo_docker = archivo_docker.replace(key, value)

        #Abre el archivo docker-compose.yaml y lo guarda.
        with open(f'../wordpress/{self.titulo}/docker-compose.yaml', 'w') as file:
            file.write(archivo_docker)

    def reemplazar_dotenv(self, contrasena_bd):
        host_bd = os.environ['WORDPRESS_DB_HOST']
        usuario_bd = self.titulo
        contrasena_bd = contrasena_bd
        nombre_bd = self.titulo
        host_virtual = self.titulo

        with open(f'../wordpress/{self.titulo}/.env', 'r') as file:
            archivo_dotenv = file.read()
            variables = {
                '$MYSQL_HOST': host_bd,
                '$MYSQL_USER': usuario_bd,
                '$MYSQL_PASSWORD': contrasena_bd,
                '$MYSQL_DATABASE': nombre_bd,
                '$VIRTUAL_HOST': host_virtual,
            }

        for key, value in variables.items():
            archivo_dotenv = archivo_dotenv.replace(key, value)
        with open(f'../wordpress/{self.titulo}/.env', 'w') as file:
            file.write(archivo_dotenv)