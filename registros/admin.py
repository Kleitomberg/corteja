from django.contrib import admin
from django.contrib.auth import admin as auth_admin


from .models import User, Perfil



@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass