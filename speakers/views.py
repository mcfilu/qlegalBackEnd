from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SpeakersSerializer
from .models import Speakers

# Create your views here.

class SpeakersView(viewsets.ModelViewSet):
    serializer_class = SpeakersSerializer
    queryset = Speakers.objects.all()
