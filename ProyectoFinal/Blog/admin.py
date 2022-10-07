from django.contrib import admin
from Blog.models import Autor, Articulo, Seccion

# Register your models here.

admin.site.register(Autor)
admin.site.register(Articulo)
admin.site.register(Seccion)
