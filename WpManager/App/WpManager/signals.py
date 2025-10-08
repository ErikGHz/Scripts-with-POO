from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Wordpress
from .tasks import crear_base_datos, crear_wordpress

@receiver(post_save, sender=Wordpress)
def post_saveWordpress(sender, instance, created, **kwargs):
    if created:
        crear_base_datos.delay(instance.titulo, instance.contrasena)
        crear_wordpress.delay(instance.titulo, instance.contrasena)