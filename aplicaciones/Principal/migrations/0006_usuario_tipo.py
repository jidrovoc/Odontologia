# Generated by Django 2.1.15 on 2022-02-15 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0005_auto_20220214_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
