from django.apps import AppConfig
from django.utils.importlib import import_module


class ImagesConfig(AppConfig):
    name = 'images'
    verbose_name = "Images"

    def ready(self):
        import_module('images.collections')
