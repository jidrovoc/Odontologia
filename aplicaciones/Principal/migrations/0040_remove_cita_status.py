# Generated by Django 2.1 on 2022-06-09 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0039_areatratamiento_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='status',
        ),
    ]
