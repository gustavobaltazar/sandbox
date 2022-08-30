from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produto
from .serializer import ProdutoSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def listar_produtos(request):
    if request.method == 'GET':
        queryset = Produto.objects.all()
        serializer = ProdutoSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

@api_view()     
def produto_detalhe(request, id):
    # try:
        produto = get_object_or_404(Produto, pk=id)
        serializer = ProdutoSerializer(produto)     
        return Response(serializer.data)
    # except Produto.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
