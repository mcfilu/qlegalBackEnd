from django.contrib import admin
from .models import Episodes

# Register your models here.
class EpisodesAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'description', 'length', 'image')

admin.site.register(Episodes, EpisodesAdmin)
