from django.core.management import BaseCommand
from catalog.models import Category
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        os.system('python3 manage.py dumpdata catalog > data.json')
        Category.objects.all().delete()
        os.system('python3 manage.py loaddata data.json ')