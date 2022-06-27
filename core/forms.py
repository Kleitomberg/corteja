from django import forms

from .models import *

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['servico', 'funcionario', 'data']
      
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['data'] = forms.DateField(label='Dia do agendaemnto', widget=forms.widgets.DateInput(attrs={'type': 'date',}))  
        
 