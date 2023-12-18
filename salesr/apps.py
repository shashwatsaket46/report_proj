from django.apps import AppConfig


class SalesrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'salesr'

    def ready(self):
        import salesr.signals
