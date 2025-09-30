from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BaseDeDatos
from .tasks import create_database

@receiver(post_save, sender=BaseDeDatos)
def handle_my_model_save(sender, instance, created, **kwargs):
    if created:
        create_database.delay(instance.nombre, instance.contrasena)