from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Image, ImageInstance
from .serializers import ImageSerializer, ImageInstanceSerializer


class ImageInstanceDocumentCollection(DRFDocumentCollection):
    model = ImageInstance
    serializer_class = ImageInstanceSerializer
    name = 'economica__image_instances'


class ImageDocumentCollection(DRFDocumentCollection):
    model = Image
    serializer_class = ImageSerializer
    name = 'economica__images'


mongodb.register(ImageDocumentCollection())
mongodb.register(ImageInstanceDocumentCollection())
