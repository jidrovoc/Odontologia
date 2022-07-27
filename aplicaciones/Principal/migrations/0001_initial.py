# Generated by Django 2.1.15 on 2022-02-08 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='areaTratamiento',
            fields=[
                ('idArea', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='historial',
            fields=[
                ('idHistorial', models.AutoField(primary_key=True, serialize=False)),
                ('tipoSangre', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('idPaciente', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('fecNacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=1)),
                ('cedula', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='tratamiento',
            fields=[
                ('idTratamiento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.FloatField(max_length=200)),
                ('idArea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.areaTratamiento')),
            ],
        ),
    ]