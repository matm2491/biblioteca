from django.shortcuts import render

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Libros
from autores.models import Autor
# Create your views here.

def libros(request):

    return render(request, 'libros/index.html')

class libreria(ListView):

    model = Libros
    

