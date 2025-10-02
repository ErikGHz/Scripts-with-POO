from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Wordpress
from .tasks import crearWordpress

@receiver(post_save, sender=Wordpress)
def post_saveWordpress(sender, instance, created, **kwargs):
    if created:
        crearWordpress.delay(instance.titulo, instance.contrasena)