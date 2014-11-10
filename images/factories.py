from random import choice, randint

import factory

# from django.contrib.contenttypes.models import ContentType
from django.contrib.webdesign.lorem_ipsum import words

# from commercia.products.models import Product


class ImageFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'images.Image'
    FACTORY_DJANGO_GET_OR_CREATE = ('url', )

    title = factory.LazyAttribute(lambda o: words(2, common=False).title())
    url = factory.LazyAttribute(
        lambda o: 'http://lorempixel.com/{}/{}/{}/'.format(
            randint(300, 600),
            randint(100, 200),
            choice([
                'abstract',
                'animals',
                'business',
                'cats',
                'city',
                'food',
                'night',
                'life',
                'fashion',
                'people',
                'nature',
                'sports',
                'technics',
                'transport'
            ])
        )
    )


class ImageInstanceFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'images.ImageInstance'
    FACTORY_DJANGO_GET_OR_CREATE = ('image', 'content_type', 'object_id')

    image = factory.SubFactory(ImageFactory)

    # This should be handled by the command now
    '''
    content_type = ContentType.objects.get(
        app_label='products',
        model='product'
    )
    object_id = factory.LazyAttribute(
        lambda o: randint(1, Product.objects.count())
    )
    '''
