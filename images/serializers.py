from rest_framework import serializers

from cqrs.serializers import CQRSSerializer

from .models import *


class ImageSerializer(CQRSSerializer):

    class Meta:
        model = Image


class ImageInstanceSerializer(CQRSSerializer):

    image = ImageSerializer()

    class Meta:
        model = ImageInstance
