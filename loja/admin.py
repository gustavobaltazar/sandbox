from django.contrib import admin
from . import models
from .models import Pedido

admin.site.register(models.Produto)
admin.site.register(models.Categoria)
admin.site.register(models.Cliente)

class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    list_display = ['item_escolhido', 'status_pagamento']
admin.site.register(Pedido, PedidoAdmin)
