from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Creator Name'))
    avatar = models.ImageField(upload_to='avatars')
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=50)
    active = models.BooleanField(default=False)
    join_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
