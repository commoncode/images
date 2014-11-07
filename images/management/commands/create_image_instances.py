import random

from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from ...factories import ImageInstanceFactory
from ...models import Image


class Command(BaseCommand):
    args = '<class> [quantity]'
    help = 'Create Image Instances'

    def handle(self, *args, **options):
        images = Image.objects.all()

        if not images.exists():
            return 'Please run ./manage create_images'

        try:
            # Split arg in module and class
            app_label, model_name = args[0].split('.')
            model = apps.get_model(app_label=app_label, model_name=model_name)
            content_type = ContentType.objects.get(
                app_label=app_label,
                model=model_name.lower()
            )
        except IndexError:
            return 'You must declare a model app_label.Model'
        except ImportError:
            return 'The class does not exists'

        try:
            quantity = args[1]
        except IndexError:
            quantity = 5

        for obj in model.objects.all():
            for i in range(quantity):
                ImageInstanceFactory(
                    content_type=content_type,
                    object_id=obj.id,
                    image=random.choice(images)
                )

            obj.save()
            print('Added Image Instance: {}'.format(obj))
