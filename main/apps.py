from django.apps import AppConfig
from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'authentication'

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
