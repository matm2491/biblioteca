from django.db import models

from autores.models import Autor
# Create your models here.

class Libros(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=False, null=False)

