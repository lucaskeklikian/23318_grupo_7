from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
# Create your views here.

from personas.models import Persona


def bienvenido(request):
    no_personas_var= Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('apellido')
    return render(request, "bienvenido.html", {"no_personas": no_personas_var,'personas': personas})

class calendarView(ListView):
    model = Persona
    template_name = "calendar.html"
