from django.contrib import admin
from .models import Preset


# Register your models here.

class PresetAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'slug', 'is_published')
    list_display_links = ('name', 'slug')
    list_editable = ('is_published',)
    search_fields = ('name', 'version')
    list_per_page = 25


admin.site.register(Preset, PresetAdmin)
