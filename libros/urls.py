from django.urls import path
from . import views

urlpatterns = [

    path('libros', views.libros, name='libros')
]