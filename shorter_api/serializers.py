from rest_framework import serializers
from shorter_api import models


class ShorterUrlSerializer(serializers.ModelSerializer):
    """Serialize Shorter Url Model"""

    class Meta:
        model = models.ShorterModelItem
        fields = ('id', 'long_url', 'hits', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True},
                        'hits': {'required': False}}


class ShorterPublicUrlSerializer(serializers.ModelSerializer):
    """Serialize Shorter Url Model"""

    class Meta:
        model = models.ShorterModelItem
        fields = ('long_url',)

