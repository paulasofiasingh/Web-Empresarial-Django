from typing import Any, List, Optional, Tuple, Union
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None): # Los 3 son parámetros que se deben pasar sí o sí
        if request.user.groups.filter(name="Personal").exists(): # Esto comprueba si dentro del grupo Personal existe el valor Usuario
        # Si en tiempo de ejecución detectamos que el usuario que está accediendo al panel de administrador forma parte del grupo Personal, readonly fields pasará a tener el valor de esta tupla
            return ('key', 'name')
        else:
        # Si no, suponemos que es cualquier otro tipo de usuario y haremos de sólo lectura created y updated como siempre
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)