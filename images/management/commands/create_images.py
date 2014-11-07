from django.core.management.base import BaseCommand

from ...factories import ImageFactory


class Command(BaseCommand):
    args = '[quantity]'
    help = 'Create Images'

    def handle(self, *args, **options):
        try:
            quantity = args[0]
        except IndexError:
            quantity = 50

        for i in range(quantity):
            image = ImageFactory()
            print('Added Image: {}'.format(image.title))
