from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class PodcastLinks(models.Model):
    name = models.CharField(_("name of the podcast media"), max_length=50)
    link = models.URLField(_("link to the podcast media page"), max_length=200)
    icon = models.ImageField(_("icon of the podcast page as on our www"), upload_to="images/podcast_icons/", null=True, blank=True)

class SocialMediaLinks(models.Model):
    name = models.CharField(_("name of the social media"), max_length=50)
    link = models.URLField(_("link to the social media"), max_length=200)
    icon = models.FileField(_("icon of the social media platform as seen on our www, in SVG FORMAT"), upload_to="images/social_icons/", null=True, blank=True)
