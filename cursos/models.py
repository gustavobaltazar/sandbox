from django.db import models


class Courses(models.Model):
  nome_curso_bosch = models.CharField(max_length=50)
  nome_curso_senai = models.CharField(max_length=50)
  duracao_bosch = models.IntegerField()
  duracao_senai = models.IntegerField()
  qtd_aprendizs = models.IntegerField()
  descritivo = models.TextField()
  mais_informacoes = models.CharField(max_length=100)

  # def __str__(self):
  #   return self.nome_curso_bosch