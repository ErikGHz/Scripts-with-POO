from django.contrib import admin
from .models import Usuario, Wordpress

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Wordpress)
class WordpressAdmin(admin.ModelAdmin):
    pass