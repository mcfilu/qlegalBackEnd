from rest_framework import serializers
from .models import Speakers

class SpeakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = ('id', 'name', 'surname', 'description', 'year', 'image', 'linkedin', 'twitter')