# Generated by Django 2.1 on 2022-06-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0034_auto_20220609_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cita',
            name='estado',
            field=models.CharField(default=12, max_length=20),
            preserve_default=False,
        ),
    ]
