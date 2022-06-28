from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):        
        return self.nome

class Horarios(Base):
    dia = models.DateField('Dia')
    horario = models.TimeField('Horario')

    def __str__(self):        
         return f'Dia:{self.dia.day} as {self.horario.hour}:{self.horario.minute}{self.horario.minute} Horas'


class Profissional(Base):
    nome = models.CharField('Cabelereiro', max_length=255)
    foto = models.ImageField('foto', upload_to="imgs/profile_user", blank=True, null=True, help_text='Foto de perfil')
    
    def __str__(self):        
       return self.nome

class Agenda(Base):
    funcionario = models.ForeignKey(Profissional, on_delete=models.PROTECT, related_name="Agendas")
    horarios = models.ManyToManyField(Horarios,  related_name="Horarios", related_query_name="horariosx")
   
    def __str__(self):        
         return f'Agenda de: {self.funcionario}'

class Agendamento(Base):
    servico = models.ForeignKey(Servicos,on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Profissional,on_delete=models.PROTECT, related_name='cabelereiro')
    dia = models.DateField('dia')
    hora = models.TimeField('hora')
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Cliente')

    def __str__(self):        
       return f'{self.servico}'