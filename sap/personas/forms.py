from django.forms import EmailInput, ModelForm, TextInput, Select, DateTimeInput, ValidationError, NumberInput
from django import forms
from personas.models import Turno, Paciente, Medico
from django.core.exceptions import NON_FIELD_ERRORS
import re

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = "__all__"
        widgets = {
            "nombre": TextInput(attrs={"type": "text", "class": "form-control"}),
            "apellido": TextInput(attrs={"type": "text", "class": "form-control"}),
            "email": EmailInput(attrs={"type": "email", "class": "form-control"}),
            "matricula": NumberInput(attrs={"type": "number", "class": "form-control"}),
        }

class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = "__all__"
        widgets = {
            "paciente": Select(attrs={"type": "select", "class": "form-select"}),
            "medico": Select(attrs={"type": "select", "class": "form-select"}),
            "fecha_y_hora": DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                "unique_together": "%(field_labels)s ya esta ocupado",
            }
        }

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            code='Invalid',
                            params={'valor':value})

def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')
    return value
    
class PacienteForm(forms.ModelForm):
    PREPAGA = (
        ("", "-Seleccione-"),
        ("OSDE", "OSDE"),
        ("SWISS", "SWISS"),
        ("OSPAT", "OSPAT"),
    )
    
    nombre = forms.CharField(
        label="Nombre",
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(
            attrs={"class": "form-control"} #"placeholder": "Ingrese su nombre"}
        ),
    )

    apellido = forms.CharField(
        label="Apellido",
        max_length=100,
        validators=(solo_caracteres,),
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    email = forms.EmailField(
        label="Email",
        max_length=100,
        required=True,
        validators=(validate_email,),
        error_messages={"required": "Por favor completa el campo"},
        widget=forms.TextInput(attrs={"class": "form-control"})#, "type": "email"}),
    )

    prepaga = forms.ChoiceField(
        label="Prepaga",
        choices= PREPAGA,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model=Paciente
        fields=['nombre','apellido','email','prepaga']


