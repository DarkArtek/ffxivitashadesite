from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='presets'),
    path('search', views.search, name='search'),
    path('preset/<slug:slug>', views.preset, name='preset')
]