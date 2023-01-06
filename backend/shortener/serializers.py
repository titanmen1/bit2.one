from rest_framework import serializers
from shortener.models import Shortener


class ShortenerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shortener
        fields = ('id', 'short_url', 'full_url', 'created_at', 'updated_at')
