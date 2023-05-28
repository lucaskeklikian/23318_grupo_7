from django.shortcuts import render, get_object_or_404, redirect
from personas.models import Turno, Paciente, Medico
from django.forms import modelform_factory
from django.core.exceptions import ValidationError
from django.contrib import messages
from personas.forms import TurnoForm, MedicoForm, PacienteForm


# Create your views here.
def eliminarTurno(request, id):
    turno = get_object_or_404(Turno, pk=id)
    if turno:
        turno.delete()
        messages.success(request,("Turno eliminado"))
    return redirect('inicio')
    

def nuevoTurno(request):
    if request.method =='POST':
        formaTurno = TurnoForm(request.POST)
        if formaTurno.is_valid:
            try:
                formaTurno.save()
                return redirect('inicio')
            except:
                messages.success(request,("Turno ocupado"))
    else: # es GET
        formaTurno = TurnoForm()

    return render(request,'personas/nuevo_turno.html',{'formaTurno':formaTurno})

def editarTurno(request, id):
    turno = get_object_or_404(Turno, pk=id)
    if request.method =='POST':
        formaTurno = TurnoForm(request.POST,instance = turno)
        if formaTurno.is_valid:
            try:
                formaTurno.save()
                return redirect('inicio')
            except:
                messages.success(request,("Fecha y hora ocupada"))
    else: # es GET
        formaTurno = TurnoForm(instance = turno)

    return render(request,'personas/editar_turno.html',{'formaTurno':formaTurno, 'turno':turno})

def detalleTurno(request, id):
    turno = get_object_or_404(Turno, pk=id)
    return render(request, 'personas/detalle_turno.html',{'turno':turno})


def nuevoPaciente(request):
    if request.method =='POST':
        formaPaciente = PacienteForm(request.POST)
        if formaPaciente.is_valid:
            try:
                formaPaciente.save()
                return redirect('inicio')
            except:
                messages.success(request,("Revise el formulario"))
    else: # es GET
        formaPaciente = PacienteForm()

    return render(request,'personas/nuevo_paciente.html',{'formaPaciente':formaPaciente})

def nuevoMedico(request):
    if request.method =='POST':
        formaMedico = MedicoForm(request.POST)
        if formaMedico.is_valid:
            try:
                formaMedico.save()
                return redirect('lista_medicos')
            except:
                messages.success(request,("Revise el formulario"))
    else: # es GET
        formaMedico = MedicoForm()

    return render(request,'personas/nuevo_medico.html',{'formaMedico':formaMedico})

def editarPaciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method =='POST':
        formaPaciente = PacienteForm(request.POST,instance = paciente)
        if formaPaciente.is_valid:
            try:
                formaPaciente.save()
                return redirect('lista_pacientes')
            except:
                messages.success(request,("No se pudo guardar Paciente"))
    else: # es GET
        formaPaciente = PacienteForm(instance = paciente)

    return render(request,'personas/editar_paciente.html',{'formaPaciente':formaPaciente})

def eliminarPaciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if paciente:
        paciente.delete()
        messages.success(request,("Paciente eliminado"))
    return redirect('lista_pacientes')

def editarMedico(request, id):
    medico = get_object_or_404(Medico, pk=id)
    if request.method =='POST':
        formaMedico = MedicoForm(request.POST,instance = medico)
        if formaMedico.is_valid:
            try:
                formaMedico.save()
                return redirect('lista_medicos')
            except:
                messages.success(request,("No se pudo guardar Medico"))
    else: # es GET
        formaMedico = MedicoForm(instance = medico)

    return render(request,'personas/editar_medico.html',{'formaMedico':formaMedico})


def eliminarMedico(request, id):
    medico = get_object_or_404(Medico, pk=id)
    if medico:
        medico.delete()
        messages.success(request,("Medico eliminado"))
    return redirect('lista_medicos')