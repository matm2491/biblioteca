from django.db import models

# Create your models here.

class Autor(models.Model):
    p_nombre = models.CharField(max_length=30, blank=True, null=True)
    p_apellidos = models.CharField(max_length=30, blank=True, null=True)
    