from multiprocessing.dummy.connection import Client
from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente, Produto, Pedido, Avaliacao, Categoria
from .serializer import ProdutoSerializer, ClienteSerializer, PedidoSerializer, AvaliacaoSerializer, CategoriaSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        return Avaliacao.objects.filter(produto_id=self.kwargs['produtos_pk'])

class ProdutoFiltro(filters.FilterSet):
    qtd_min = filters.NumberFilter(field_name="estoque", lookup_expr='gte')

    class Meta:
        model = Produto
        fields=['categoria_id', 'estoque']

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria_id', 'estoque']
    filterset_class = ProdutoFiltro
    # def get_queryset(self):
    #     queryset = Produto.objects.all()
    #     categoria_id = self.request.query_params.get('categoria_id')
    #     if categoria_id is not None:
    #         queryset = queryset.filter(categoria_id=categoria_id)
    #     return queryset

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# class ListarProduto(ListCreateAPIView):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer

#     def create(self, request, *args, **kwargs):
#         if float(request.data['preco']) < 0 or float(request.data['preco']) > 400:
#             return Response({
#                 "ERROR!": "Só é possível cadastrar produtos com o preço abaixo de 400 e maior que 0"
#             })
#         return super().create(request, *args, **kwargs)

# class ProdutoDetalhe(RetrieveUpdateDestroyAPIView):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer
#     # lookup_field = 'id'
#     def update(self, request, *args, **kwargs):
#         if float(request.data['preco']) < 0 or float(request.data['preco']) > 400:
#             return Response({
#                 "ERROR!": "Só é possível cadastrar produtos com o preço abaixo de 400"
#             })
#         return super().update(request, *args, **kwargs)

#     def delete(self, pk):
#         produto = get_object_or_404(Produto, pk=pk)
#         if produto.estoque > 0:
#             return Response({
#                 "ERROR": "Só é possível deletar produtos com estoque zerado!"
#             })
#         produto.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # @api_view(['GET', 'POST'])
# # def listar_avaliacao(request):
# #     if request.method == 'GET':
# #         queryset = Avaliacao.objects.all()
# #         serializer = AvaliacaoSerializer(queryset, many=True)
# #         return Response(serializer.data, status=status.HTTP_200_OK)
# #     elif request.method == 'POST':
# #         serializer = AvaliacaoSerializer(data=request.data)
# #         if serializer.is_valid(raise_exception=True):
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         else: 
# #             return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

# class ListarAvaliacao(ListCreateAPIView):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer

# class AvaliacaoDetalhe(RetrieveUpdateDestroyAPIView):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer


# # @api_view(['GET', 'POST'])
# # def listar_produtos(request):
# #     if request.method == 'GET':
# #         queryset = Produto.objects.all()
# #         serializer = ProdutoSerializer(queryset, many=True)
# #         return Response(serializer.data)

# #     elif request.method == 'POST':
# #         serializer = ProdutoSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         else: 
# #             return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

# # @api_view(['GET', 'PUT', 'DELETE'])     
# # def produto_detalhe(request, id):
# #     produto = get_object_or_404(Produto, pk=id)

# #     if request.method == 'GET':
# #         serializer = ProdutoSerializer(produto)     

# #         return Response(serializer.data)

# #     elif request.method == 'PUT':
# #         serializer = ProdutoSerializer(produto, data=request.data)    
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(status=status.HTTP_200_OK)

# #     elif request.method == 'DELETE':
# #         produto.delete()

# #         return Response(status=status.HTTP_204_NO_CONTENT)

# class ListarCliente(ListCreateAPIView):
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializer

# class ClienteDetalhe(RetrieveUpdateDestroyAPIView):
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializer

# # @api_view(['GET', 'POST'])
# # def listar_clientes(request):
# #     if request.method == 'GET':
# #         queryset = Cliente.objects.all()
# #         serializer = ClienteSerializer(queryset, many=True)
# #         return Response(serializer.data)

# #     elif request.method == 'POST':
# #         serializer = ClienteSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(status=status.HTTP_201_CREATED)

# #     else:
# #         return Response(status=status.HTTP_400_BAD_REQUEST)

# # @api_view(['GET','PUT','DELETE'])
# # def cliente_detalhe(request, id):
# #     cliente = get_object_or_404(Cliente, pk=id)
# #     if request.method == 'GET':
# #         serializer = ClienteSerializer(cliente)
# #         return Response(serializer.data)
# #     elif request.method == 'PUT':
# #         serializer = ClienteSerializer(Cliente, data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(status=status.HTTP_200_OK)
# #     else:
# #         cliente.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)
        
# class ListarPedido(ListCreateAPIView):
#     queryset = Pedido.objects.all()
#     serializer_class = PedidoSerializer

# class PedidoDetalhe(RetrieveUpdateDestroyAPIView):
#     queryset = Pedido.objects.all()
#     serializer_class = PedidoSerializer
    
# # @api_view(['GET', 'POST'])
# # def listar_pedidos(request):
# #     if request.method == 'GET':
# #         queryset = Pedido.objects.all()
# #         serializer = PedidoSerializer(queryset, many=True)
# #         return Response(serializer.data)

# #     elif request.method == 'POST':
# #         serializer = PedidoSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(status=status.HTTP_201_CREATED)

# #     else:
# #         return Response(status=status.HTTP_400_BAD_REQUEST)

# # @api_view(['GET', 'PUT', 'DELETE'])
# # def pedido_detalhe(request, id):
# #     pedido = get_object_or_404(Pedido, pk=id)

# #     if request.method == 'GET':
# #         serializer = PedidoSerializer(Pedido)
# #         return Response(serializer.data)

# #     elif request.method == 'PUT':
# #         serializer = PedidoSerialzier(Pedido, data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(status=status.HTTP_200_OK)
# #     else:
# #         pedido.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)

