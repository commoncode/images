import factory

from django.contrib.webdesign.lorem_ipsum import paragraphs, words

from faker import Factory

fake = Factory.create()


class ImageFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'images.Image'

    title = factory.LazyAttribute(lambda o: words(2, common=False).title())


class ImageInstanceFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'images.ImageInstance'

    image = factory.SubFactory(ImageFactory)
