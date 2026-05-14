from django.apps import AppConfig
import os

class BreedConfig(AppConfig):
    name = 'Breed'

    def ready(self):
        if os.environ.get('RUN_MAIN') == 'true':
            from .scheduler import start
            start()
