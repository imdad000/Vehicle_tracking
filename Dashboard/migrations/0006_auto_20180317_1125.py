# Generated by Django 2.0.3 on 2018-03-17 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0005_auto_20180317_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_detail',
            name='vehicle_status',
            field=models.CharField(choices=[('1', '1'), ('0', '0'), ('-1', '-1')], default='-1', max_length=10),
        ),
    ]
