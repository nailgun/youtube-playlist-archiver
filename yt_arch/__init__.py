import os

from django.apps import AppConfig


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yt_arch.settings')


class App(AppConfig):
    name = 'yt_arch'
