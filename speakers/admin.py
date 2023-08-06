from django.contrib import admin
from .models import Speakers

# Register your models here.
class SpeakersAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'description', 'year', 'image', 'linkedin', 'twitter')

admin.site.register(Speakers, SpeakersAdmin)