# Generated by Django 4.2 on 2023-05-03 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0005_remove_persona_fecha_remove_persona_hora_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha_y_hora',
            field=models.DateTimeField(blank=True, error_messages=False, null=True, unique=True),
        ),
    ]