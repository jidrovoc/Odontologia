# Generated by Django 2.1 on 2022-05-29 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0029_auto_20220525_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alergia',
            name='nombre',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='alergia',
            name='observacion',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
