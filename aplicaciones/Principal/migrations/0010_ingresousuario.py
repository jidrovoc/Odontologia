# Generated by Django 2.1.15 on 2022-02-24 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0009_historial_descripciontratamiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='ingresoUsuario',
            fields=[
                ('idIngreso', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('idUsuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Principal.usuario')),
            ],
        ),
    ]
