# Generated by Django 4.2.10 on 2024-02-29 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0007_alter_bus_departure_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='departure_time',
            field=models.DateField(),
        ),
    ]