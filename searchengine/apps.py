from django.apps import AppConfig
from searchengine import pdfutility

class SearchengineConfig(AppConfig):
    name = 'searchengine'

    def ready(self):
        pdfutility.extractText()


