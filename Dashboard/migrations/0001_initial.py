# Generated by Django 2.0.3 on 2018-03-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=60)),
                ('driver_contact_number', models.BigIntegerField()),
                ('vehilce_number', models.CharField(max_length=60)),
                ('vehicle_location_latitute', models.CharField(max_length=40)),
                ('vehicle_location_altitute', models.CharField(max_length=40)),
                ('vehicle_status', models.IntegerField()),
            ],
        ),
    ]