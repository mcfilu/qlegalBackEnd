from django.db import models
from django.utils.translation import gettext as _

def link_upload_to(instance, filename):
    return "/files/team/{}".format(filename)

# Create your models here.
class Team(models.Model):
    name = models.CharField(_("team member name"), max_length=50)
    surname = models.CharField(_("team member surname"), max_length=50)
    position = models.CharField(_("position in the project"), max_length=50)
    description = models.TextField(_("description of the team member"))
    year = models.IntegerField(_("year the team member was in"))
    image = models.ImageField(_("picture of the team member"), upload_to='images/team/')
    linkedin = models.URLField(_("link to team member linkedin profile"), max_length=200, null=True, blank=True)
    twitter = models.URLField(_("link team member twitter profile"), max_length=200, null=True, blank=True)