import datetime
from django.views.generic import ListView
from time import time
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin,GroupRequiredMixin

from .models import Agendamento

from .forms import*



class IndexView(TemplateView):
    template_name = 'index.html'

class CriarAgendamento(LoginRequiredMixin, CreateView):
      template_name = 'agendamentos/create.html'
      form_class = AgendamentoForm
      success_url = reverse_lazy('index')
      login_url = reverse_lazy('account_login')


      def post(self, request, *args, **kwargs):
        obj = dict(self.get_form_kwargs()['data'])
        print('****', obj)
       
        
        #polo = objects.all()    
        agendamento = Agendamento(
                                     
             data=request.POST.get('data'),
            
        )
       
        f = request.POST.get('funcionario')
        print(f' cliquei emmm {f}')
       
        agendamento.cliente = self.request.user
        agendamento.funcionario=Profissional.objects.get(pk=f)
            
        agendamento.servico=Servicos.objects.get(pk=obj['servico'][0])
        agendamento.save()
        
    
     
        return HttpResponseRedirect(self.success_url)
      
      def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.request)
        #
        # id_polo = self.request.POST.get("id_polo")
        # print(f'idPolo {id_polo}')
        
        context['funcionarios'] = Profissional.objects.all()
        context['horariosM'] = Horarios.objects.all()[:5]
        context['horariosT'] = Horarios.objects.all()[5:]
        context['horariosT'] = Horarios.objects.all()[5:]
       
        return context



class AgendaListView(ListView):
    model = Agenda
    template_name = 'agendamentos/create.html'    
               
    def get_queryset(self):
        queryset = Agenda.objects.all()
                      
        return queryset
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   

        return context
