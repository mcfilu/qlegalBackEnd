from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NewsletterSerializer
from .models import Newsletter

# Create your views here.

class NewsletterView(viewsets.ModelViewSet):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()