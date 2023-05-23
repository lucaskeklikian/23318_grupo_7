from django.db import models

# Create all your models here.

class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'
    
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # fecha = models.DateField(null=True, blank=True)
    # hora = models.TimeField(null=True, blank=True)
    fecha_y_hora = models.DateTimeField(null=True,blank=True,unique=True,error_messages={"unique":"Fecha y hora ocupada"})
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)
   
    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'

 