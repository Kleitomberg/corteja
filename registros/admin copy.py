from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import Perfil



@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass