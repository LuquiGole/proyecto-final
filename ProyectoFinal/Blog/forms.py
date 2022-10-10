from typing import TextIO
from django import forms

class ArticuloForm (forms.Form):
    titulo = forms.CharField(max_length=50)
    texto = forms.CharField(max_length=1000)
    fecha_publicacion =  forms.DateField()


class AutorForm (forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    profesion = forms.CharField(max_length=50)


class SeccionForm (forms.Form):
    nombre = forms.CharField(max_length=50)

