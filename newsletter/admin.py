from django.contrib import admin
from .models import Newsletter

# Register your models here.
class NewsletterAdmin(admin.ModelAdmin):
    display_list = ('name', 'email')

admin.site.register(Newsletter, NewsletterAdmin)