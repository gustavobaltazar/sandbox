from django.contrib import admin
from . import models
from .models import Avaliacao, Pedido

admin.site.register(models.Produto)
admin.site.register(models.Categoria)
admin.site.register(models.Cliente)
class AvaliacaoProduto(admin.ModelAdmin):
    model = Avaliacao
    list_display = ['produto', 'nome', 'estrelas']

admin.site.register(Avaliacao, AvaliacaoProduto)

class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    list_display = ['item_escolhido', 'status_pagamento', 'cliente_pedido']
admin.site.register(Pedido, PedidoAdmin)

