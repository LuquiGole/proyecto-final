from django.shortcuts import render
from Blog.models import Autor, Articulo, Seccion
from Blog.forms import ArticuloForm, SeccionForm, AutorForm
# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def buscar(request):
    if request.method == "GET": 
        return render(request, "busqueda.html")
    if request.method == "POST":
        titulo_para_buscar = request.POST["titulo"]
        modelos = Articulo.objects.filter(titulo=titulo_para_buscar)
        contexto = {"resultados" : modelos}
        return render(request, "resultadobusqueda.html", context = contexto)


def autores(request):
    if request.method == "GET": 
        mi_formulario = AutorForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "autores.html",context= contexto)

    if request.method == "POST":
        mi_formulario = AutorForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Autor(
                nombre = datos_ingresados_por_usuario["nombre"],
                apellido = datos_ingresados_por_usuario["apellido"],
                profesion = datos_ingresados_por_usuario["profesion"],
            )
            nuevo_modelo.save()
            return render(request, "exito.html")
        contexto = {"formulario": mi_formulario}
        return render(request, "autores.html",context= contexto)

def articulos(request):
    if request.method == "GET": 
        mi_formulario = ArticuloForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "articulos.html",context= contexto)

    if request.method == "POST":
        mi_formulario = ArticuloForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Articulo(
                titulo = datos_ingresados_por_usuario["titulo"],
                texto = datos_ingresados_por_usuario["texto"],
                fecha_publicacion = datos_ingresados_por_usuario["fecha_publicacion"],
            )
            nuevo_modelo.save()
            return render(request, "exito.html")
        contexto = {"formulario": mi_formulario}
        return render(request, "articulos.html",context= contexto)


def secciones(request):
    if request.method == "GET": 
        mi_formulario = SeccionForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "secciones.html",context= contexto)

    if request.method == "POST":
        mi_formulario = SeccionForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Seccion(
                nombre = datos_ingresados_por_usuario["nombre"],
            )
            nuevo_modelo.save()
            return render(request, "exito.html")
        contexto = {"formulario": mi_formulario}
        return render(request, "secciones.html",context= contexto)