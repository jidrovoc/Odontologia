# Generated by Django 2.1 on 2022-06-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0047_auto_20220609_1038'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='estadocuenta',
            name='abono',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='estadocuenta',
            name='saldo',
            field=models.IntegerField(null=True),
        ),
    ]
