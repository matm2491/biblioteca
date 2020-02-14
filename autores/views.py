from django.shortcuts import render

# Create your views here.

def autores(request):

    return render(request, 'autores/autores.html')