from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from personas.models import Turno, Paciente, Medico
from django.contrib.auth.decorators import login_required
from .filters import TurnoFilter

# Create your views here.
@login_required
def lista_turnos(request):
    nro_turnos= Turno.objects.count()
    turnos = Turno.objects.order_by('fecha_y_hora')

    myfilter = TurnoFilter(request.GET,queryset=turnos)
    turnos = myfilter.qs
    return render(request, "lista_turnos.html", {"nro_turnos": nro_turnos,'turnos' : turnos,'myFilter': myfilter})

@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.order_by('apellido')
    return render(request, "lista_pacientes.html", {'pacientes':pacientes})

@login_required
def lista_medicos(request):
    medicos = Medico.objects.order_by('apellido')
    return render(request, "lista_medicos.html", {'medicos':medicos})

class calendarView(ListView):
    model = Turno
    template_name = "calendar.html"
