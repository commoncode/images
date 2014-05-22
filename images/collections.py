from cqrs.mongo import mongodb
from cqrs.collections import DRFDocumentCollection

from .models import Image
from .serializers import ImageSerializer, ImageInstanceSerializer


class ImageInstanceDocumentCollection(DRFDocumentCollection):
    model = Image
    serializer_class = ImageInstanceSerializer
    name = 'image_instances'


class ImageDocumentCollection(DRFDocumentCollection):
    model = Image
    serializer_class = ImageSerializer
    name = 'images'


mongodb.register(ImageDocumentCollection())
mongodb.register(ImageInstanceDocumentCollection())
