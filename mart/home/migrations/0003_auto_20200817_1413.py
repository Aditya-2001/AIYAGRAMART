# Generated by Django 3.0.8 on 2020-08-17 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200816_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufacturing_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 17, 14, 13, 29, 532993)),
        ),
    ]
