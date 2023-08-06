from django.db import models
from django.utils.translation import gettext as _
from django.dispatch import receiver
from django.db.models.signals import post_save
import os
from django.conf import settings

def link_upload_to():
    return ""

# Create your models here.
class Episodes(models.Model):
    title = models.CharField(_("tile of the episode"), max_length=150)
    published_date = models.DateField(_("episode publish date"), auto_now=False, auto_now_add=False)
    description = models.TextField(_("description of episode"))
    image = models.FileField(_("image used as a episode cover image"), upload_to="images/episodes/")
    length = models.IntegerField(_("length of podcast in seconds"))
    spotify_link = models.URLField(_("spotify link to this episode"), max_length=200, null=True, blank=True)
    apple_link = models.URLField(_("apple link to this episode"), max_length=200, null=True, blank=True)
    overcast_link = models.URLField(_("overcast link to this episode"), max_length=200, null=True, blank=True)
    buzzsprout_link = models.URLField(_("buzzsprout link to this episode"), max_length=200, null=True, blank=True)

    def _str_(self):
        return self.title

