from socket import AI_PASSIVE
from django.db import models

class Endereco(models.Model):
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_lenght=100)
    rua = models.CharField(max_length= 100)
    
class Usuario(models.Model):
    cpf = models.CharField(max_length=15)

class Cliente(models.Model):
   nome = models.CharField(max_length=50)
   idade = models.DecimalField(max_digits=2)
   cliente_endereco = models.ForeignKey(Endereco, related_name='Endereco', on_delete=models.CASCADE)

class Cartao(models.Model):
    pass

class Conta(models.Model):
    carteira = models.DecimalField(max_digits=7, decimal_places=2)
    cartao_conta = models.ForeignKey(Cartao, related_name='Cartao', on_delete=models.CASCADE)

class Fatura(models.Model):
    pass

class Transacao(models.Model):
    pass

class Emprestimo(models.Model):
    pass

class PagEmprestimo(models.Model):
    pass

class Favorito(models.Model):
    pass

class Extrato(models.model):
    pass