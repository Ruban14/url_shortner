from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate/url', views.generate_url, name='generate_url'),
    path('serve/shortned/url', views.serve_shorten_url, name='serve_shorten_url'),

]