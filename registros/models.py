from django.db import models

from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Perfil')
    telefone = PhoneNumberField(unique = True, null = True, blank = True)   
    foto = models.ImageField('foto', upload_to="imgs/profile_user", blank=True, null=True, help_text='Foto de perfil')
   
    def __str__(self):
        return self.user.username