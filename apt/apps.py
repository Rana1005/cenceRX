from django.apps import AppConfig


class AptConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apt'

    def ready(self):
        from jobs import updater
        updater.start()
        return super().ready()
