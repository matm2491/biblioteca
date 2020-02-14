from django.contrib import admin
from libros.models import Libros
from autores.models import Autor
# Register your models here.

class LibreriasAdmin(admin.ModelAdmin):

    list_display=("nombre", "autor")
    #search_fields=("primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido")

admin.site.register(Libros)
admin.site.register(Autor)

