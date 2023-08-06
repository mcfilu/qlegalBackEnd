from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EpisodesSerializer
from .models import Episodes

# Create your views here.

class EpisodesView(viewsets.ModelViewSet):
    serializer_class = EpisodesSerializer
    queryset = Episodes.objects.all()