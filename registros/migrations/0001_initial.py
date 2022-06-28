# Generated by Django 4.0.4 on 2022-06-28 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True)),
                ('foto', models.ImageField(blank=True, help_text='Foto de perfil', null=True, upload_to='imgs/profile_user', verbose_name='foto')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
