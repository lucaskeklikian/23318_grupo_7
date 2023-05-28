# Generated by Django 4.2 on 2023-05-24 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0014_alter_turno_fecha_y_hora'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='turno',
            name='turno unico',
        ),
        migrations.AddConstraint(
            model_name='turno',
            constraint=models.UniqueConstraint(fields=('paciente', 'medico', 'fecha_y_hora'), name='turno_ocupado', violation_error_message='Turno ocupado'),
        ),
        migrations.AddConstraint(
            model_name='turno',
            constraint=models.UniqueConstraint(fields=('paciente', 'fecha_y_hora'), name='paciente_fecha_hora_ocupada', violation_error_message='Paciente Fecha y hora ocupada'),
        ),
        migrations.AddConstraint(
            model_name='turno',
            constraint=models.UniqueConstraint(fields=('medico', 'fecha_y_hora'), name='medico_fecha_hora_ocupada', violation_error_message='Medico Fecha y hora ocupada'),
        ),
    ]