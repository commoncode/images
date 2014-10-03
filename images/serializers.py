from cqrs.serializers import CQRSSerializer

from .models import Image, ImageInstance


class ImageSerializer(CQRSSerializer):

    class Meta:
        model = Image


class ImageInstanceSerializer(CQRSSerializer):

    image = ImageSerializer()

    class Meta:
        model = ImageInstance
