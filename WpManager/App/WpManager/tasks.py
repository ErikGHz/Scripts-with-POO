from celery import shared_task
from .scripts.createDatabase import BaseDeDatos
from .scripts.createWordpress import Wordpress

@shared_task
def my_task():
    
    print('Hello from Celery!')
    
    return

@shared_task
def crear_base_datos(titulo, contrasena) -> None:
    nueva_bd = BaseDeDatos()
    nueva_bd.conectar_servidor()
    nueva_bd.crear_recursos(titulo, contrasena)

@shared_task
def crear_wordpress(titulo, contrasena) -> None:
    nuevo_wordpress = Wordpress(titulo)
    nuevo_wordpress.crear_directorio()
    nuevo_wordpress.copiar_docker()
    nuevo_wordpress.reemplazar_docker()
    nuevo_wordpress.reemplazar_dotenv(contrasena)
    nuevo_wordpress.inciar_docker()
