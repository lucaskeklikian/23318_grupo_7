from django.db import models
from django.core.exceptions import ValidationError

# Create all your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    matricula = models.IntegerField(verbose_name="matricula")
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    prepaga = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True)
    fecha_y_hora = models.DateTimeField(null=True)
        
    def __str__(self):
        return f'Paciente: {self.paciente} - Medico: {self.medico} - Fecha y Hora: {self.fecha_y_hora}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["paciente", "medico", "fecha_y_hora"], name='turno_ocupado',violation_error_message = 'Turno ocupado'),
            models.UniqueConstraint(fields=["paciente", "fecha_y_hora"], name='paciente_fecha_hora_ocupada',violation_error_message = 'Paciente Fecha y hora ocupada'),
            models.UniqueConstraint(fields=["medico", "fecha_y_hora"], name='medico_fecha_hora_ocupada',violation_error_message = 'Medico Fecha y hora ocupada')
        ]
    
    