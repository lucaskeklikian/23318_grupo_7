from django.contrib import admin
from personas.models import Paciente, Medico, Turno


# Register your models here.

# admin.site.register(Paciente)
# admin.site.register(Medico)
admin.site.register(Turno)

class TurnoInline(admin.TabularInline):
    model=Turno
    readonly_fields = ('paciente', 'medico','fecha_y_hora')
    extra = 1




@admin.register(Paciente,Medico)
class PacienteAdmin(admin.ModelAdmin):
    inlines = [TurnoInline]