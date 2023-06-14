import django_filters
#from django_filters import Charfilter
from personas.models import *


class TurnoFilter(django_filters.FilterSet):
    paciente = django_filters. ModelChoiceFilter(queryset=Paciente.objects.all().order_by('apellido'))
    medico = django_filters. ModelChoiceFilter(queryset=Medico.objects.all().order_by('apellido'))

    class Meta:
        model = Turno
        fields = '__all__'
        exclude = ['fecha_y_hora']


