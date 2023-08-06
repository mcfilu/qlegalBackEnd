from django.db import models
from django.utils.translation import gettext as _

def link_upload_to(instance, filename):
    return "/files/speakers/{}".format(filename)

# Create your models here.
class Speakers(models.Model):
    name = models.CharField(_("speakers name"), max_length=50)
    surname = models.CharField(_("speakers surname"), max_length=50)
    description = models.TextField(_("description of the speaker"))
    year = models.IntegerField(_("year the speaker took part"))
    image = models.ImageField(_("picture of the speaker"), upload_to='images/speakers/')
    linkedin = models.URLField(_("link to speakers linkedin profile"), max_length=200, null=True, blank=True)
    twitter = models.URLField(_("link speakers twitter profile"), max_length=200, null=True, blank=True)

# class Receivers(models.Model):
#     user = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
#     name = models.CharField(_("receivers name"), max_length=50)