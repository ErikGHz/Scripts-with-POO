from celery import shared_task
from .createDatabase import BasedeDatos
import time

@shared_task
def create_database(nombre, contrasena):
    nuevaBD = BasedeDatos()
    nuevaBD.conectarServidor()
    nuevaBD.crearRecursos(nombre, contrasena)
    print("Base de datos creada")
    time.sleep(10)

    return

@shared_task
def hola():
    print("hola")

    return