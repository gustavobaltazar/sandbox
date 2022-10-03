from random import choices
from django.db import models
import uuid


class Usuario(models.Model):
    NORMAL = 'N'
    GOLD = 'G'
    PLATINUM = 'P'

    TIPOS_CONTA = [
        (NORMAL, 'Normal'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpf = models.CharField(max_length=15)
    senha = models.CharField(max_length=100)
    tipo_conta = models.CharField(max_length=1, choices=TIPOS_CONTA)

    def __str__(self) -> str:
        return self.cpf

class Cliente(models.Model):
    SEXO_MASCULINO = 'M'
    SEXO_FEMININO = 'F'

    SEXO_TIPOS = [
        (SEXO_MASCULINO, 'Male'),
        (SEXO_FEMININO, 'Female'),
    ]

    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_TIPOS)

    def __str__(self) -> str:
        return self.nome
        


class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)


class Cartao(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    numero_cartao = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    validade = models.DateField()

    def __str__(self) -> str:
        return self.numero_cartao


class Conta(models.Model):
    ATIVO = 'A'
    NAO_ATIVO = 'N'

    CONTA_ATIVA = [
        (ATIVO, 'A'),
        (NAO_ATIVO, 'N')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carteira = models.DecimalField(max_digits=20, decimal_places=5)
    cartao_conta = models.ForeignKey(
        Cartao, related_name='Cartao', on_delete=models.CASCADE)
    conta_ativa = models.CharField(max_length=1, choices=CONTA_ATIVA)

    def __str__(self) -> str:
        return self.cliente


class Fatura(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    STATUS_PAGO = 'P'
    STATUS_NAO_PAGO = 'NP'

    STATUS_PAGAMENTO = [
        (STATUS_PAGO, 'P'),
        (STATUS_NAO_PAGO, 'NP'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=20, decimal_places=2)
    parcelas = models.IntegerField()
    data_pagamento = models.DateField()
    status_pagamento = models.CharField(max_length=2, choices=STATUS_PAGAMENTO)

    list_display = [cliente, parcelas, data_pagamento, status_pagamento]

class Transacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TED = 'TE'
    DOC = 'DO'
    BOLETO = 'BO'
    VOUCHER = 'VO'
    DUPLICATAS = 'DU'

    TIPO_TRANSACAO = [
        (TED, 'TE'),
        (DOC, 'DO'),
        (BOLETO, 'BO'),
        (VOUCHER, 'VO'),
        (DUPLICATAS, 'DU'),
    ]

    transacao = models.CharField(max_length=2, choices=TIPO_TRANSACAO)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING, related_name='cliente')
    beneficiado = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING, related_name='beneficiado')
    data_transacao = models.DateField()
    valor_transferido = models.DecimalField(max_digits=20, decimal_places=2)


class Emprestimo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente_pedido = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING, related_name='cliente_pedido')
    cliente_emprestou = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING, related_name='cliente_emprestou')
    data_pagamento = models.DateField()


class PagEmprestimo(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.DO_NOTHING, related_name='emprestimo')
    parcelas = models.IntegerField()
    juros = models.DecimalField(max_digits=2, decimal_places=2)


class Favorito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente_favoritado = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)


class Extrato(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    emprestimo_feito = models.ForeignKey(Emprestimo, on_delete=models.DO_NOTHING)
    transacao_feita = models.ForeignKey(Transacao, on_delete=models.DO_NOTHING)
    fatura_obtida = models.ForeignKey(Fatura, on_delete=models.DO_NOTHING)