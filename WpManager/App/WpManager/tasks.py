from celery import shared_task
from .models import Usuario
from .scripts.createDatabase import BaseDeDatos

@shared_task
def my_task():
    
    print('Hello from Celery!')
    
    return

@shared_task
def crearWordpress(titulo, contrasena) -> bool:
    nueva_bd = BaseDeDatos()
    nueva_bd.conectarServidor()
    nueva_bd.crearRecursos(titulo, contrasena)