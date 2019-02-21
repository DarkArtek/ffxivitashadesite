import random
import os
from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


# Create your models here.

def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_path(instance, filename):
    new_filename = random.randint(1, 6851461946)
    name, ext = get_file_ext(filename)
    final_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "img/avatars/{new_filename}/{final_name}".format(new_filename=new_filename, final_name=final_name)


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Creator Name'))
    avatar = models.ImageField(upload_to=upload_path)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=50)
    active = models.BooleanField(default=False)
    join_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
