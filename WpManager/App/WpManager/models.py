from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    apellido_paterno = models.CharField("Apellido paterno", max_length=50)
    apellido_materno = models.CharField("Apellido materno", max_length=50)
    correo = models.EmailField("Correo electronico", unique=True)
    nombre_usuario = models.CharField("Nombre de usuario", max_length=33)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

class Wordpress(models.Model):
    titulo = models.CharField("Título del sitio", max_length=100, unique=True)
    nombre_usuario = models.CharField("Nombre de usuario del administrador", max_length=50)
    contrasena = models.CharField("Contraseña", max_length=128)  # Idealmente cifrada
    correo = models.EmailField("Correo del administrador")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nombre = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo}"