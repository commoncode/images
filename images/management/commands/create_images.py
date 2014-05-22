from random import choice

from django.core.management.base import BaseCommand, CommandError

from ...factories import ImageFactory


class Command(BaseCommand):
    help = 'Create Images'

    def handle(self, *args, **options):
        print "Creating Images"

        for i in range(5):
            image = ImageFactory()
            print "Added Image: {}".format(image.title)
