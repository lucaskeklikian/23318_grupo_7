# Generated by Django 4.2 on 2023-05-03 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0010_alter_persona_fecha_y_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha_y_hora',
            field=models.DateTimeField(blank=True, error_messages={'unique': False}, null=True, unique=True),
        ),
    ]
