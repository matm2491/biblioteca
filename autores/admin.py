from django.contrib import admin
from libros.models import Libros
from autores.models import Autor
# Register your models here.

class LibreriasAdmin(admin.ModelAdmin):

    list_display=("nombre", "autor")
    search_fields=("p_nombre", "p_apellidos")

admin.site.register(Libros)
admin.site.register(Autor)

