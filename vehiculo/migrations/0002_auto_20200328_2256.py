# Generated by Django 3.0.4 on 2020-03-29 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehiculopapeles',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]