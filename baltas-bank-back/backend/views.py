from tabnanny import check
from django import views
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import viewsets
from rest_framework import status
from backend.models import Conta, Endereco, Usuario, Cliente, Cartao
from backend.serializer import CartaoSerializer, ContaSerializer, EnderecoSerializer, UsuarioSerializer, ClienteSerializer
from rest_framework.response import Response


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        cpf = request.data['cpf']

        if len(cpf) > 11 or len(cpf) < 0:
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

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def create(self, request, *args, **kwargs):
        cliente = Cliente.objects.get()
        cidade = request.data['cidade']
        bairro = request.data['bairro']
        estado = request.data['estado']
        rua = request.data['rua']
        data = Endereco(cliente=cliente, cidade=cidade, estado=estado, bairro=bairro, rua=rua)
        data.save()
        return Response({'detalhe': 'Endereço adicionado com sucesso!'}, status=status.HTTP_201_CREATED)


class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

    def create(self, request, *args, **kwargs):
        numero_cartao = request.data['numero_cartao']
        cvv = request.data['cvv']
        limite = request.data['limite']
        validade = request.data['validade']
        data = Cartao(numero_cartao=numero_cartao, cvv=cvv,
                      limite=limite, validade=validade)
        data.save()
        return Response({'detalhe': 'Cartão adicionado com sucesso!'}, status=status.HTTP_201_CREATED)


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

    def create(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(id)
        carteira = request.data['carteira']
        cartao_conta = Cartao.objects.get()
        conta_ativa = request.data['conta_ativa']
        data = Conta(cliente=cliente, carteira=carteira,
                     cartao_conta=cartao_conta, conta_ativa=conta_ativa)
        data.save()
        return Response({'detalhe': 'Conta criada com sucesso!'}, status=status.HTTP_201_CREATED)
