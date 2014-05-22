from random import randint

import factory

from django.contrib.contenttypes.models import ContentType
from django.contrib.webdesign.lorem_ipsum import paragraphs, words

from faker import Factory

fake = Factory.create()


class ImageFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'images.Image'

    title = factory.LazyAttribute(lambda o: words(2, common=False).title())
    url = factory.LazyAttribute(lambda o: 'http://placehold.it/{}x{}'.format(
        randint(300, 600), randint(100, 200)))


class ImageInstanceFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'images.ImageInstance'

    image = factory.SubFactory(ImageFactory)

    content_type = ContentType.objects.first() # Let's just ram it up
    object_id = 1
