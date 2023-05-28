from django.contrib import admin
from personas.models import Paciente, Medico, Turno


# Register your models here.

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Turno)