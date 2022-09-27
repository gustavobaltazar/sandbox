from random import choices
from django.db import models


class Endereco(models.Model):
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_lenght=100)
    rua = models.CharField(max_length=100)


class Usuario(models.Model):
    GOLD = 'G'
    PLATINUM = 'P'
    NORMAL = 'N'

    CARD_TYPES = [
        (NORMAL, 'Normal'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum'),
    ]
    cpf = models.CharField(max_length=15)
    senha = models.CharField(max_length=100)
    tipo_conta = models.CharField(max_length=1, )

class Cliente(models.Model):
    SEXO_MASCULINO = 'M'
    SEXO_FEMININO = 'F'

    SEXO_TIPOS = [
        (SEXO_MASCULINO, 'Male'),
        (SEXO_FEMININO, 'Female'),
    ]
    nome = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idade = models.DecimalField(max_digits=2)
    sexo = models.CharField(max_length=1, choices=SEXO_TIPOS)
    cliente_endereco = models.ForeignKey(Endereco, related_name='Endereco', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user_name

class Cartao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    numero_cartao = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    validade  = models.DateField() 
   
    def __str__(self) -> str:
        return self.numero_cartao 
class Conta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carteira = models.DecimalField(max_digits=20, decimal_places=5)
    cartao_conta = models.ForeignKey(Cartao, related_name='Cartao', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.cliente

class Fatura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=20, decimal_places=2)
    parcelas = models.IntegerField()

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