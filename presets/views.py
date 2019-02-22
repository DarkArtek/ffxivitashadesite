from django.shortcuts import render, get_object_or_404
from .models import Preset
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import version_choices


# Create your views here.

def index(request):
    listings = Preset.objects.order_by('-preset-date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'presets/listings.html', context)


def preset(request, slug):
    preset = get_object_or_404(Preset, slug=slug)
    context = {
        'preset': preset,
    }
    return render(request, 'presets/preset.html', context)


def search(request):
    queryset_list = Preset.objects.order_by('-preset-date')
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'version' in request.GET:
        version = request.GET['version']
        if version:
            queryset_list = queryset_list.filter(version__lte=version)

    context = {
        'keywords': keywords,
        'version': version,
        'values': request.GET,
    }

    return render(request, 'presets/search.html', context)
