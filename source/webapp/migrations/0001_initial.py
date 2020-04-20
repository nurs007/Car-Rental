# Generated by Django 3.0.5 on 2020-04-20 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25, verbose_name='Car brand:')),
                ('name', models.CharField(max_length=255, verbose_name='Car name:')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price:')),
                ('description', models.CharField(max_length=1500, verbose_name='Car description:')),
                ('photo', models.ImageField(upload_to='car_images', verbose_name='Car photo:')),
                ('transmission', models.CharField(choices=[('M', 'Manual'), ('A', 'Automatic')], default='M', max_length=50, verbose_name='Transmission:')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car', to=settings.AUTH_USER_MODEL, verbose_name='Author:')),
            ],
        ),
        migrations.CreateModel(
            name='CarCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Car category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Last name')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last updated')),
                ('cars', models.ManyToManyField(related_name='orders', to='webapp.Car', verbose_name='Cars')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oders', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='OrderCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cars', to='webapp.Car', verbose_name='Car')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cars', to='webapp.Order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Car booking',
                'verbose_name_plural': 'Cars booking',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='car_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='webapp.CarCategory', verbose_name='Car category:'),
        ),
    ]
