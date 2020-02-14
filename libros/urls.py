from django.urls import path
from libros.views import libreria
from . import views

urlpatterns = [

    path('libros', views.libros, name='libros'),
    path('index', libreria.as_view(template_name = "libros/index.html"), name='index')
]