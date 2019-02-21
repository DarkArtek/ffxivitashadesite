from django.shortcuts import render
from django.http import HttpResponse
from presets.models import Preset
from presets.choices import version_choices


# Create your views here.

def index(request):
    presets = Preset.objects.order_by('-date').filter(is_published=True)[:3]
    context = {
        'presets': presets,
        'version': version_choices
    }

    return render(request, 'pages/../templates/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
