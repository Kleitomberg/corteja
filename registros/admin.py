from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User, Perfil


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
   
    list_display = ('id','username','telefone')




@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass