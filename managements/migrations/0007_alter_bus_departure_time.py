# Generated by Django 4.2.10 on 2024-02-27 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0006_bus_depart_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='departure_time',
            field=models.DateTimeField(),
        ),
    ]
