from django.contrib import admin

from .models import Cartao, Cliente, Conta, Usuario

class UsuarioLista(admin.ModelAdmin):
    model = Usuario
    list_display = ['cpf', 'tipo_conta']

admin.site.register(Usuario, UsuarioLista)

class ClienteLista(admin.ModelAdmin):
    model = Cliente
    list_display = ['nome', 'sobrenome', 'idade']

admin.site.register(Cliente, ClienteLista)


class CartaoLista(admin.ModelAdmin):
    model = Cartao
    list_display = ['numero_cartao', 'validade']

admin.site.register(Cartao, CartaoLista)

class ContaLista(admin.ModelAdmin):
    model = Conta
    list_display = ['cliente', 'carteira', 'conta_ativa']
admin.site.register(Conta, ContaLista)
