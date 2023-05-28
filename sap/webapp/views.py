from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from personas.models import Turno, Paciente, Medico

# Create your views here.

def bienvenido(request):
    nro_turnos= Turno.objects.count()
    turnos = Turno.objects.order_by('fecha_y_hora')
    return render(request, "bienvenido.html", {"nro_turnos": nro_turnos,'turnos' : turnos})

def lista_pacientes(request):
    pacientes = Paciente.objects.order_by('apellido')
    return render(request, "lista_pacientes.html", {'pacientes':pacientes})

def lista_medicos(request):
    medicos = Medico.objects.order_by('apellido')
    return render(request, "lista_medicos.html", {'medicos':medicos})

class calendarView(ListView):
    model = Turno
    template_name = "calendar.html"
