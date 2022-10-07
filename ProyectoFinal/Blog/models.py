from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    

class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    
class Tema(models.Model):
    nombre = models.CharField(max_length=50)