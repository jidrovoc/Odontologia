# Generated by Django 2.1 on 2022-06-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0032_paciente_estadocivil'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='estado',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]