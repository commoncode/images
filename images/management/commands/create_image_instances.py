from random import choice

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from ...factories import ImageInstanceFactory
from ...models import Image


class Command(BaseCommand):
    help = 'Create Image Instances'

    def handle(self, *args, **options):
        print "Creating Image Instances"

        images = Image.objects.all()

        if not images.exists():
            call_command('create_images')

        for image in images:
            ImageInstanceFactory(image=image)
            print "Added Image Instance: {}".format(image.title)
