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
class Pedido(models.Model):
    pedido = models.CharField(max_length=255)
    descricao = models.TextField()
    quantidade = models.PositiveSmallIntegerField()
    
class PedidoItem(models.Model):
    pass