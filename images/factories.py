from random import randint

import factory

from django.contrib.contenttypes.models import ContentType
from django.contrib.webdesign.lorem_ipsum import paragraphs, words

from commercia.products.models import Product

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

    content_type = ContentType.objects.get(app_label='products',
        model='product')
    object_id = factory.LazyAttribute(lambda o: randint(1,
        Product.objects.count()))
