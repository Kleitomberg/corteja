# Generated by Django 4.0.4 on 2022-06-28 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('dia', models.DateField(verbose_name='Dia')),
                ('horario', models.TimeField(verbose_name='Horario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=255, verbose_name='Cabelereiro')),
                ('foto', models.ImageField(blank=True, help_text='Foto de perfil', null=True, upload_to='imgs/profile_user', verbose_name='foto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Seriço')),
                ('duracao', models.IntegerField(verbose_name='Duração aproximada')),
                ('valor', models.IntegerField(verbose_name='Valor do Serviço')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('data', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cliente', to=settings.AUTH_USER_MODEL)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cabelereiro', to='core.profissional')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.servicos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.profissional')),
                ('horarios', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.horarios')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
