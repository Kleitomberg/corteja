from django.contrib import admin


from .models import *



@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    pass


@admin.register(Horarios)
class HorariosAdmin(admin.ModelAdmin):
    pass

@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    pass


@admin.register(Agenda)
class ServicosAdmin(admin.ModelAdmin):
    pass


@admin.register(Agendamento)
class ServicosAdmin(admin.ModelAdmin):
     radio_fields = {"funcionario": admin.HORIZONTAL}
