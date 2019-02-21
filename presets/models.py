import random
import os
from autoslug.settings import slugify
from django.db import models
from django.utils import timezone
from creators.models import Author


# Create your models here.

def get_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_preset_bg_path(instance, filename):
    new_filename = random.randint(1, 6851461946)
    name, ext = get_ext(filename)
    final_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "img/presets-bg/{new_filename}/{final_name}".format(new_filename=new_filename, final_name=final_name)


def upload_preset_image_path(instance, filename):
    new_filename = random.randint(1, 6851461946)
    name, ext = get_ext(filename)
    final_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "img/presets-images/{new_filename}/{final_name}".format(new_filename=new_filename, final_name=final_name)


class Preset(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150, unique=True)
    bg_image = models.ImageField(upload_to=upload_preset_bg_path)
    description = models.TextField()
    img_1 = models.ImageField(upload_to=upload_preset_image_path, blank=True)
    img_2 = models.ImageField(upload_to=upload_preset_image_path, blank=True)
    img_3 = models.ImageField(upload_to=upload_preset_image_path, blank=True)
    img_4 = models.ImageField(upload_to=upload_preset_image_path, blank=True)
    img_5 = models.ImageField(upload_to=upload_preset_image_path, blank=True)
    img_6 = models.ImageField(upload_to=upload_preset_image_path, blank=True)
    img_7 = models.ImageField(upload_to=upload_preset_image_path, blank=True)
    img_8 = models.ImageField(upload_to=upload_preset_image_path, blank=True)
    is_published = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.preset_slug = slugify(self.name)
        super(Preset, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
