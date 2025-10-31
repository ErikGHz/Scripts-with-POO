import time
from celery import shared_task
from .scripts.createDatabase import BaseDeDatos
from .scripts.createWordpress import Wordpress
from .scripts.llenar_formulario import Selenium

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

@shared_task
def formulario_wordpress(titulo, usuario, correo) -> None:
    time.sleep(2)
    timeout = 60
    start_time = time.time()
    wordpress = Wordpress(titulo)
    while True:
        if wordpress.docker_healthcheck() == 'healthy':
                print("WordPress listo")
                rellenar_formulario = Selenium(titulo, usuario, correo)
                rellenar_formulario.instalacion_wordpress()
                break
        elif time.time() - start_time > timeout:
            print('Wordpress aun no esta listo')
        time.sleep(1)