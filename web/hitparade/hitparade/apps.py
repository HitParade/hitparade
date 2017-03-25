from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "hitparade"

    def ready(self):
        import_module("hitparade.receivers")
