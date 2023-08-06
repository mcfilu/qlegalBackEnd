from rest_framework import serializers
from .models import Episodes

class EpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields = ('id', 'title', 'published_date', 'description', 'image', 'length', 'spotify_link', 'apple_link', 'overcast_link', 'buzzsprout_link')