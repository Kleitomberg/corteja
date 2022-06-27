from django.contrib.auth import forms
from django import forms as f

from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

from allauth.account.forms import SignupForm

from .models import User, Perfil



class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User


class CustomSignupForm(SignupForm):
    class Meta:
        model = User    
        exclude =('base','ativo')    
        fields = '__all__'       

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        
           
            self.fields['telefone'] = f.CharField(max_length=100,
                                                        widget=f.TextInput(attrs={'placeholder': 'XXXXXXXXXXX'}))

                        
            self.fields['foto'] = f.ImageField(required=False, label=" ", help_text="Foto de perfil")

                    
    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)        

       
        #user.bio = self.cleaned_data['bio']
        user.telefone = self.cleaned_data['telefone']        
        user.foto = self.cleaned_data['foto']
               

        perfil = Perfil.objects.create(
            user = user
        )
        perfil.save()

        nameGroup ='cliente'
        print(nameGroup)
        grupo = get_object_or_404(Group,name=nameGroup)
        user.groups.add(grupo)

           
        user.save()
       
        return user

    def form_valid(self, form):

        nameGroup ='cliente'
        grupo = get_object_or_404(Group,name=nameGroup)
        print(nameGroup)
        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        return url
    


class EditProfileForm(f.ModelForm):


    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            
            self.fields['telefone'] = f.CharField(max_length=100,
                                                        widget=f.TextInput(attrs={'placeholder': '87996759869'}))
            
            self.fields['foto'] = f.ImageField(required=False, label=" ", help_text="Foto de perfil",  widget=f.FileInput)

            
                                     

    class Meta:
        model = User    
        exclude =('base','ativo')    
        fields = '__all__' 
    


class EditPictureForm(f.ModelForm):

    class Meta:
        model = User
        exclude =('base','ativo') 
        fields = ['foto']
