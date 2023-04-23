from django.forms import EmailInput, ModelForm, DateInput, TimeInput, TextInput, Select,ChoiceField
from personas.models import Persona, Domicilio


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'type':'text','class':'form-control'}),
            'apellido': TextInput(attrs={'type':'text','class':'form-control'}),
            'email': EmailInput(attrs={'type':'email','class':'form-control'}),
            'fecha': DateInput(attrs={'type': 'date','class':'form-control'}),
            'hora' : TimeInput(attrs={'type':'time','class':'form-control'}),
            'domicilio': Select(attrs={'type':'select','class':'form-select'}), 
        }
