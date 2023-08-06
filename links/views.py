from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PodcastLinksSerializer, SocialMediaLinksSerializer
from .models import PodcastLinks, SocialMediaLinks

# Create your views here.

class PodcastLinksView(viewsets.ModelViewSet):
    serializer_class = PodcastLinksSerializer
    queryset = PodcastLinks.objects.all()

class SocialMediaLinksView(viewsets.ModelViewSet):
    serializer_class = SocialMediaLinksSerializer
    queryset = SocialMediaLinks.objects.all()
