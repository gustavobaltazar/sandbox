from django.contrib import admin

from .models import Cliente, Usuario

class UsuarioLista(admin.ModelAdmin):
    model = Usuario
    list_display = ['cpf', 'tipo_conta']

admin.site.register(Usuario, UsuarioLista)

class ClienteLista(admin.ModelAdmin):
    model = Cliente
    list_display = ['nome', 'sobrenome', 'idade']

admin.site.register(Cliente, ClienteLista)
