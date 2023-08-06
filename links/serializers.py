from rest_framework import serializers
from .models import PodcastLinks, SocialMediaLinks

class PodcastLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastLinks
        fields = ('id', 'name', 'link', 'icon')

class SocialMediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinks
        fields = ('id', 'name', 'link', 'icon')