# Generated by Django 2.1.15 on 2022-02-26 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0013_auto_20220225_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='consulta',
            fields=[
                ('idConsulta', models.AutoField(primary_key=True, serialize=False)),
                ('motivo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='tratamientoTemporal',
            fields=[
                ('idTratamientoTemporal', models.AutoField(primary_key=True, serialize=False)),
                ('idPaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.paciente')),
                ('idTratamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.tratamiento')),
            ],
        ),
        migrations.AddField(
            model_name='tratamientorealizado',
            name='idConsulta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Principal.consulta'),
            preserve_default=False,
        ),
    ]
