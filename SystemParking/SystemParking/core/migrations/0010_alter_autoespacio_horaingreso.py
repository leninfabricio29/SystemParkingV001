# Generated by Django 3.2.12 on 2023-06-09 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_autoespacio_horaingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoespacio',
            name='horaIngreso',
            field=models.DateField(blank=True, verbose_name=datetime.datetime(2023, 6, 9, 3, 54, 42, 889631)),
        ),
    ]
