from django.contrib import admin
from .models import PodcastLinks, SocialMediaLinks

# Register your models here.
class PodcastLinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')

class SocialMediaLinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')

admin.site.register(PodcastLinks, PodcastLinksAdmin)
admin.site.register(SocialMediaLinks, SocialMediaLinksAdmin)
