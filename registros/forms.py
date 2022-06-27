from django.contrib.auth import forms
from django import forms as f

from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

from allauth.account.forms import SignupForm

from .models import  Perfil


