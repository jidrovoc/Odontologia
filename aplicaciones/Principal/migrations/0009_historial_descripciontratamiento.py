# Generated by Django 2.1.15 on 2022-02-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0008_cita_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='descripcionTratamiento',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
