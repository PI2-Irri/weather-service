# Generated by Django 2.2.5 on 2019-09-15 03:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_time', models.DateTimeField(default=datetime.datetime.now)),
                ('temperature', models.FloatField(default=0.0)),
                ('temperature_min', models.FloatField(default=0.0)),
                ('temperature_max', models.FloatField(default=0.0)),
                ('wind_velocity', models.FloatField(default=0.0)),
                ('rain_precipitation', models.FloatField(blank=True, default=0.0, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Location')),
            ],
        ),
        migrations.CreateModel(
            name='ForecastMeasurement',
            fields=[
                ('measurement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='measurements.Measurement')),
            ],
            bases=('measurements.measurement',),
        ),
        migrations.CreateModel(
            name='MinutelyMeasurement',
            fields=[
                ('measurement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='measurements.Measurement')),
            ],
            bases=('measurements.measurement',),
        ),
    ]