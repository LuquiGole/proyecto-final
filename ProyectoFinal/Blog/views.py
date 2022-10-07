from django.shortcuts import render
from Blog.models import Autor, Articulo, Seccion

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")
