# Generated by Django 3.0.8 on 2020-08-29 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200829_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 29, 16, 45, 7, 185565)),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturing_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 29, 16, 45, 7, 184211)),
        ),
        migrations.AlterField(
            model_name='usersorders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 29, 16, 45, 7, 186124)),
        ),
    ]
