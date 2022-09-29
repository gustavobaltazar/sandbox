from tabnanny import check
from django import views
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import viewsets
from rest_framework import status
from backend.models import Usuario
from backend.serializer import UsuarioSerializer
from rest_framework.response import Response


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        cpf = request.data['cpf']
        
        if len(cpf) > 11:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
            
        senha = request.data['senha']
        tipo_conta = request.data['tipo_conta']
        senha_encriptada = make_password(senha)
        print(senha_encriptada)
        # check_senha = check_password(
        #     senha, senha_encriptada)
        # print(check_senha)
        data = Usuario(cpf=cpf, senha=senha_encriptada, tipo_conta=tipo_conta)
        data.save()

        return Response(status=status.HTTP_201_CREATED)
