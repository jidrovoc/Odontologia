# Generated by Django 2.1.15 on 2022-02-26 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0016_remove_historial_descripciontratamiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='idCita',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Principal.cita'),
            preserve_default=False,
        ),
    ]
