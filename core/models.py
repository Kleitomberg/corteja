from tkinter import CASCADE
from django.db import models

# Create your models here.
class Base(models.Model):
    class Meta:
        abstract = True

    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de modificação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

class Servicos(Base):
    nome = models.CharField('Nome do Seriço', max_length=255)
    duracao = models.IntegerField('Duração aproximada')
    valor = models.IntegerField('Valor do Serviço')

class Horarios(Base):
    horario = models.TimeField('Horario')


class Profissional(Base):
    nome = models.CharField('Cabelereiro', max_length=255)
    horarios = models.ForeignKey(Horarios, on_delete=models.CASCADE)

class Agendamento(Base):
    pass