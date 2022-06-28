from django.urls import path


from .views import *

urlpatterns = [  
     path('', IndexView.as_view(), name='index'),
     path('agendamentos/criar', CriarAgendamento.as_view(), name='criar_agendamentos'),
     path('getAgenda/<int:pk>', AgendaListView.as_view(), name='pegaAgenda'),
] 