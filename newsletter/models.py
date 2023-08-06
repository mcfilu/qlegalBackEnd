from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Newsletter(models.Model):
    name = models.CharField(_("person name"), max_length=50)
    email = models.EmailField(_("person email"), max_length=254)