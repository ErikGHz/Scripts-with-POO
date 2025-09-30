from django.apps import AppConfig


class DbmanagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DbManager'

    def ready(self):
        import DbManager.signals