from autoslug.settings import slugify
from django.db import models
from django.utils import timezone
from creators.models import Author


# Create your models here.

class Preset(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150, unique=True)
    bg_image = models.ImageField(upload_to='bg-images')
    description = models.TextField()
    img_1 = models.ImageField(upload_to='presets-images', blank=True)
    img_2 = models.ImageField(upload_to='presets-images', blank=True)
    img_3 = models.ImageField(upload_to='presets-images', blank=True)
    img_4 = models.ImageField(upload_to='presets-images', blank=True)
    img_5 = models.ImageField(upload_to='presets-images', blank=True)
    img_6 = models.ImageField(upload_to='presets-images', blank=True)
    img_7 = models.ImageField(upload_to='presets-images', blank=True)
    img_8 = models.ImageField(upload_to='presets-images', blank=True)
    is_published = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.preset_slug = slugify(self.name)
        super(Preset, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
