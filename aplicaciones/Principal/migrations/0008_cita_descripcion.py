# Generated by Django 2.1.15 on 2022-02-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0007_auto_20220216_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='descripcion',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
