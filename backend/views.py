from tabnanny import check
from django import views
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import viewsets
from rest_framework import status
from backend.models import Usuario, Cliente, Cartao
from backend.serializer import CartaoSerializer, UsuarioSerializer, ClienteSerializer
from rest_framework.response import Response


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        cpf = request.data['cpf']

        if len(cpf) > 11 or len(cpf) <0:
            return Response({'detalhe': 'Número de dígitos inválido!'}, status=status.HTTP_401_UNAUTHORIZED)

        senha = request.data['senha']
        tipo_conta = request.data['tipo_conta']
        senha_encriptada = make_password(senha)
        # check_senha = check_password(
        #     senha, senha_encriptada)
        # print(check_senha)
        data = Usuario(cpf=cpf, senha=senha_encriptada, tipo_conta=tipo_conta)
        data.save()

        return Response({'detalhe': 'Usuario criadocom sucesso!'}, status=status.HTTP_201_CREATED)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def create(self, request, *args, **kwargs):
        nome = request.data['nome']
        sobrenome = request.data['sobrenome']
        usuario = Usuario.objects.get()
        idade = request.data['idade']
        sexo = request.data['sexo']
        data = Cliente(nome=nome, sobrenome=sobrenome,
                       usuario=usuario, idade=idade, sexo=sexo)
        data.save()
        return Response({'detalhe': 'Cliente adicionado com sucesso!'}, status=status.HTTP_201_CREATED)

class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

    def create(self, request, *args, **kwargs):
        numero_cartao = request.data['numero_cartao']
        cvv = request.data['cvv']
        limite = request.data['limite']
        validade = request.data['validade']
        data = Cartao(numero_cartao=numero_cartao, cvv=cvv, limite=limite, validade=validade)
        data.save()
        return super().create(request, *args, **kwargs)
