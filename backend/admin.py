from django.contrib import admin

from .models import Usuario

class UsuarioLista(admin.ModelAdmin):
    model = Usuario
    list_display = ['cpf', 'tipo_conta']

admin.site.register(Usuario, UsuarioLista)
