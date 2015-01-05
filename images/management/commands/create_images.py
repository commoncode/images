from random import randint

from django.core.management.base import BaseCommand

from images.factories import ImageFactory


class Command(BaseCommand):
    args = '<type> [quantity]'
    help = (
        'Image types: book | cosmetic | food | garment | software | vehicle'
    )

    def handle(self, *args, **options):
        try:
            category = {
                'book': 'business',
                'cosmetic': 'people',
                'food': 'food',
                'garment': 'fashion',
                'software': 'technics',
                'vehicle': 'transport'
            }.get(args[0].lower())
        except IndexError:
            return (
                'Please declare a type of image, read help for available '
                'options.'
            )

        try:
            quantity = int(args[1])
        except IndexError:
            quantity = randint(20, 30)

        print('Creating Images')

        for i in range(quantity):
            url = 'http://lorempixel.com/{width}/{height}/{category}'.format(
                width=randint(100, 500),
                height=randint(100, 500),
                category=category

            )
            ImageFactory(url=url)
            print(url)
