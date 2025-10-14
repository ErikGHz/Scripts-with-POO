import subprocess, os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Wordpress:
    def __init__(self, titulo):
        self.titulo = titulo

    def crear_directorio(self):
        nombre_directorio = self.titulo
        subprocess.run(["sh",  f"{BASE_DIR}/scripts/createwordpress.sh", "crear_directorio", BASE_DIR, nombre_directorio])

    def copiar_docker(self):
        nombre_directorio = self.titulo
        subprocess.run(["sh",  f"{BASE_DIR}/scripts/createwordpress.sh", "copiar_docker", BASE_DIR, nombre_directorio])

    def reemplazar_docker(self):
        nombre_servicio = self.titulo
        nombre_contenedor = self.titulo
        #Abre el archivo docker-compose.yaml y define un diccionario de variables
        with open(f'{BASE_DIR}/wordpress/{self.titulo}/docker-compose.yaml', 'r') as file:
            archivo_docker = file.read()
            variables = {
            '$SERVICE_NAME': nombre_servicio,
            '$CONTAINER_NAME': nombre_contenedor,
            }
        #Sustituye las variables del diccionario
        for key, value in variables.items():
            archivo_docker = archivo_docker.replace(key, value)

        #Abre el archivo docker-compose.yaml y lo guarda.
        with open(f'{BASE_DIR}/wordpress/{self.titulo}/docker-compose.yaml', 'w') as file:
            file.write(archivo_docker)

    def reemplazar_dotenv(self, contrasena_bd):
        host_bd = os.environ['WORDPRESS_DB_HOST']
        usuario_bd = self.titulo
        contrasena_bd = contrasena_bd
        nombre_bd = self.titulo
        host_virtual = self.titulo

        with open(f'{BASE_DIR}/wordpress/{self.titulo}/.env', 'r') as file:
            archivo_dotenv = file.read()
            variables = {
                '$MYSQL_HOST': host_bd,
                '$MYSQL_USER': usuario_bd,
                '$MYSQL_PASSWORD': contrasena_bd,
                '$MYSQL_DATABASE': nombre_bd,
                '$VIRTUAL_HOST': host_virtual.lower(),
            }

        for key, value in variables.items():
            archivo_dotenv = archivo_dotenv.replace(key, value)
        with open(f'{BASE_DIR}/wordpress/{self.titulo}/.env', 'w') as file:
            file.write(archivo_dotenv)

    def inciar_docker(self):
        nombre_directorio = self.titulo
        subprocess.run(["sh",  f"{BASE_DIR}/scripts/createwordpress.sh", "iniciar_docker", BASE_DIR, nombre_directorio])
        pass

    def docker_healthcheck(self) -> str:
        nombre_directorio = self.titulo
        command = f"docker inspect {nombre_directorio} --format '{{{{.State.Health.Status}}}}'"
        output_command = subprocess.check_output(command, shell=True)
        health = output_command.decode().strip()
        if health == 'healthy':
            print('healthy')
        elif health == 'unhealthy':
            print('unhealthy')
        else:
            print('starting')
        return health