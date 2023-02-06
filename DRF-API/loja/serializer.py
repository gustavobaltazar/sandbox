from dataclasses import fields
from decimal import Decimal
from rest_framework import serializers
from loja.models import Categoria, Cliente, Pedido, Produto, Avaliacao

# class ProdutoSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     titulo = serializers.CharField(max_length=255)
#     preco = serializers.DecimalField(max_digits=6, decimal_places=2)
#     preco_taxado = serializers.SerializerMethodField(method_name='calcular_taxa')

#     def calcular_taxa(self, produto : Produto):
#         return produto.preco * Decimal(1.1)

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'titulo', 'preco', 'preco_taxado', 'estoque', 'categoria']

    preco_taxado = serializers.SerializerMethodField(method_name='calcular_taxa')

    def calcular_taxa(self, produto : Produto):
        return produto.preco * Decimal(1.1)

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields=['id','nome', 'cpf', 'email']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id','dt_pedido', 'status_pagamento', 'cliente_pedido']

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        # fields = '__all__'
        fields = ['id', 'produto', 'nome', 'descricao', 'dt_avaliacao', 'estrelas']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields= ['categoria']