# Generated by Django 3.0.5 on 2020-04-20 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordercar',
            name='car',
        ),
        migrations.RemoveField(
            model_name='ordercar',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderCar',
        ),
    ]
