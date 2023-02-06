from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.categoria


class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    decritivo = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.PositiveSmallIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.titulo


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.nome

class Pedido(models.Model):
    STATUS_PAGO = 'P'
    STATUS_CANCELADO = 'C'
    STATUS_AGUARDANDO = 'A'

    STATUS_PG = [
        (STATUS_AGUARDANDO, 'Aguardando'),
        (STATUS_CANCELADO, 'Cancelado'),
        (STATUS_PAGO, 'Pago'),
    ]

    dt_pedido = models.DateTimeField(auto_now_add=True)
    status_pagamento = models.CharField(max_length=1, choices=STATUS_PG, default='STATUS_AGUARDANDO')
    cliente_pedido = models.ForeignKey(Cliente, related_name='Nome', on_delete=models.CASCADE)
    item_escolhido = models.ForeignKey(Produto, related_name='Produto', on_delete=models.CASCADE)


class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='item', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='produto', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    qtd = models.PositiveSmallIntegerField()
        
class Avaliacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    dt_avaliacao = models.DateField(auto_now_add=True)
    estrelas = models.PositiveSmallIntegerField()