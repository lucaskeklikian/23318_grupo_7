# Generated by Django 4.2 on 2023-04-22 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_persona_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='hora',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
