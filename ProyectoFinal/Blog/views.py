from django.shortcuts import render
from Blog.models import Autor, Articulo, Seccion

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def autores(request):
    return render(request, "autores.html")


def articulos(request):
    return render(request, "articulos.html")


def secciones(request):
    return render(request, "secciones.html")
