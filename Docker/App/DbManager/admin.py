from django.contrib import admin
from .models import BaseDeDatos

# Register your models here.
@admin.register(BaseDeDatos)
class BaseDeAdmin(admin.ModelAdmin):
    pass