from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Wordpress
from .tasks import crear_base_datos, crear_wordpress
import random, string

@receiver(post_save, sender=Wordpress)
def post_saveWordpress(sender, instance, created, **kwargs):
    if created:
        contrasena = generar_contrasena()
        crear_base_datos.delay(instance.titulo, contrasena)
        crear_wordpress.delay(instance.titulo, contrasena)


def generar_contrasena() -> str:
    letras = string.ascii_letters
    digitos = string.digits

    cadena = letras + digitos
    length = 16
    return "".join(random.sample(cadena, length))