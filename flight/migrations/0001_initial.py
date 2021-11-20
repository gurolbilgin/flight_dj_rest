# Generated by Django 3.2.9 on 2021-11-20 19:00

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
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightNumber', models.IntegerField()),
                ('operatingAirlines', models.CharField(max_length=25)),
                ('departureCity', models.CharField(max_length=30)),
                ('arrivalCity', models.CharField(max_length=30)),
                ('dateOfDeparture', models.DateField()),
                ('estimatedTimeOfDeparture', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.IntegerField()),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservarion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='flight.flight')),
                ('passenger', models.ManyToManyField(related_name='passenger', to='flight.Passenger')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
