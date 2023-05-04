from django.shortcuts import render, get_object_or_404, redirect
from personas.models import Persona
from django.forms import modelform_factory
from django.core.exceptions import ValidationError
from django.contrib import messages


from personas.forms import PersonaForm
# Create your views here.

def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html',{'persona':persona})

#PersonaForm = modelform_factory(Persona, exclude=[]) # a partir del modelo persona genera una clase PersonaForm

def nuevaPersona(request):
    if request.method =='POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid:
            try:
                formaPersona.save()
                return redirect('inicio')
            except:
                messages.success(request,("Fecha y hora ocupada"))
                
    else: # es GET
        formaPersona = PersonaForm()

    return render(request,'personas/nuevo.html',{'formaPersona':formaPersona})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method =='POST':
        formaPersona = PersonaForm(request.POST,instance= persona)
        if formaPersona.is_valid:
            try:
                formaPersona.save()
                return redirect('inicio')
            except:
                messages.success(request,("Fecha y hora ocupada"))
    else: # es GET
        formaPersona = PersonaForm(instance = persona)

    return render(request,'personas/editar.html',{'formaPersona':formaPersona})   

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('inicio')
    