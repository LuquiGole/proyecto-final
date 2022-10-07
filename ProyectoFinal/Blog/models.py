from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)


class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=1000)
    fecha_publicacion = models.DateField(null=True)


class Seccion(models.Model):
    nombre = models.CharField(max_length=50)
