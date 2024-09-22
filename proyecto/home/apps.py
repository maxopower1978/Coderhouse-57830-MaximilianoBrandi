from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

class YourAppConfig(AppConfig):
    name = 'your_app' 

    def ready(self):
        import your_app.signals  # Importa tus señales
