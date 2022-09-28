from django.contrib import admin

from .models import Usuario

class UsuarioLista(admin.ModelAdmin):
    model = Usuario
    fields = ['all']

admin.site.register(Usuario, UsuarioLista)
