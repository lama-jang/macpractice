# Generated by Django 3.1.5 on 2021-03-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuelcost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelinfo',
            name='efficiency',
            field=models.FloatField(null=True),
        ),
    ]