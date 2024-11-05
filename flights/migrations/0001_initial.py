# Generated by Django 5.1.2 on 2024-11-05 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airline', '0001_initial'),
        ('airports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.FloatField(blank=True, default=0.0, null=True)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flights', to='airline.airline')),
                ('destiny_airport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='destiny_airport', to='airports.airports')),
                ('origin_airport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='origin_airport', to='airports.airports')),
            ],
        ),
    ]
