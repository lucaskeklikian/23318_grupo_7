"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from webapp.views import lista_turnos, calendarView, lista_pacientes, lista_medicos
from personas.views import detalleTurno, nuevoTurno, nuevoPaciente, nuevoMedico, editarTurno, editarPaciente, editarMedico, eliminarTurno, eliminarPaciente, eliminarMedico
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista_turnos',lista_turnos, name='inicio'),
    path('lista_pacientes',lista_pacientes, name='lista_pacientes'),
    path('lista_medicos',lista_medicos, name='lista_medicos'),
    path('nuevo_paciente', nuevoPaciente,name='nuevo_paciente'),
    path('nuevo_medico', nuevoMedico,name='nuevo_medico'),
    path('nuevo_turno', nuevoTurno, name='nuevo_turno'),
    path('editar_paciente/<int:id>', editarPaciente),
    path('editar_medico/<int:id>', editarMedico),
    path('editar_turno/<int:id>', editarTurno),
    path('detalle_turno/<int:id>', detalleTurno),
    path('eliminar_turno/<int:id>', eliminarTurno),
    path('eliminar_paciente/<int:id>', eliminarPaciente),
    path('eliminar_medico/<int:id>', eliminarMedico),
    path('calendar/', login_required(calendarView.as_view()),name='calendar'),
    path('members/', include('django.contrib.auth.urls')),
    path('', include('members.urls'))
]
